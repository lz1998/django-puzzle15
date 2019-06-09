from django.shortcuts import render
from django.http import *
from mobile.models import *
import requests, json

APPID = "101560284"
RANK_LIST_SIZE = 10


# Create your views here.

def set_user(request):
    userid = request.GET.get("userid")
    user, created = User.objects.update_or_create(userid=userid)
    user.access_token = request.GET.get("access_token")
    user.expires_time = request.GET.get("expires_time")
    params = {
        "openid": user.userid,
        "access_token": user.access_token,
        "oauth_consumer_key": APPID
    }
    qq_info = requests.get(url="https://graph.qq.com/user/get_user_info", params=params)
    qq_info = json.loads(qq_info.text)
    user.nickname = qq_info['nickname']
    user.figureurl = qq_info['figureurl_qq']
    user.save()
    ret = {
        'status': True
    }
    return JsonResponse(ret)
    try:
        pass
    except Exception as e:
        ret = {
            'status': False
        }
        return JsonResponse(ret)


def set_result(request):
    try:
        userid = request.GET.get("userid")

        result_record, created = Result.objects.update_or_create(user_id=userid)
        result_record.result = request.GET.get("result")
        result_record.moves = request.GET.get("moves")
        result_record.time = request.GET.get("time")
        result_record.save()

        ret = {
            'status': True
        }
        return JsonResponse(ret)
    except Exception as e:
        ret = {
            'status': False
        }
        return JsonResponse(ret)


def index(request):
    a = {
        'asd': 1234
    }
    return JsonResponse(a)


def get_rank(request):
    try:
        # 取排行前RANK_LIST_SIZE名
        rst_list = []
        result_list = Result.objects.filter(result__isnull=False).order_by("result")[:RANK_LIST_SIZE]
        for result in result_list:
            rst_list.append({
                "userid": result.user.userid,
                "nickname": result.user.nickname,
                "figureurl": result.user.figureurl,
                "moves": result.moves,
                "result": result.result,
                "time": result.time
            })
        ret = {
            'status': True,
            'rst_size': len(rst_list),
            'rst': rst_list
        }

        # 如果参数有userid，取个人排名
        userid = request.GET.get("userid")
        user_result = Result.objects.filter(user_id=userid).first()
        if userid and user_result:
            ret.update({"user_result": {
                "userid": user_result.user.userid,
                "nickname": user_result.user.nickname,
                "figureurl": user_result.user.figureurl,
                "moves": user_result.moves,
                "result": user_result.result,
                "time": user_result.time
            }})
            user_rank = Result.objects.filter(result__isnull=False).filter(result__lt=user_result.result).count() + 1
            ret.update({"user_rank": user_rank})

        return JsonResponse(ret)
    except Exception as e:
        ret = {
            'status': False
        }
        return JsonResponse(ret)
