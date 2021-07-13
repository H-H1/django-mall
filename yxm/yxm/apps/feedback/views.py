from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feedback.models import Feedback
from feedback.serializer import FeedbackSerializer


class FeedbackView(CreateAPIView):
    """保存反馈"""
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) #反序列化输入
        serializer.is_valid(raise_exception=True)
        try:
            user = request.user
            contents = request.data["content"]
            type = request.data["type"]
            c = Feedback()
            c.user_id = user.id
            c.content = contents
            c.type = type
            c.username = user.username
            c.save()
        except Exception:
            return Response({"message": "提交留言失败"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "提交留言成功"}, status=status.HTTP_201_CREATED)
