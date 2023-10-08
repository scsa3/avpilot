from django.shortcuts import render

from django.http import StreamingHttpResponse
import os


def stream_mp4(request):
    mp4_file = open("/Users/weihan/PycharmProjects/avpilot/dummy/upload/Big_Buck_Bunny_360_10s_1MB.mp4", 'rb')

    response = StreamingHttpResponse(mp4_file, content_type='video/mp4')
    response['Content-Length'] = os.path.getsize("/Users/weihan/PycharmProjects/avpilot/dummy/upload/Big_Buck_Bunny_360_10s_1MB.mp4")

    return response