from rest_framework import serializers

from feedback.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """提交反馈的序列化器"""
    class Meta:
        model = Feedback
        fields = ('id', 'content', 'type') #额外校验
        extra_kwargs = {
            'content': {
                'min_length': 10,
                'max_length': 255,
                'error_messages': {
                    'min_length': '仅允许10-255个字符',
                    'max_length': '仅允许10-255个字符',
                }
            },
            'type': {
                'min_length': 1,
                'max_length': 6,
                'error_messages': {
                    'min_length': '仅允许1-6个字符的终端名称',
                    'max_length': '仅允许1-6个字符的终端名称',
                }
            },
        }