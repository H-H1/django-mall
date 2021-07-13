import xadmin

from feedback.models import Feedback

class FeedbackAdmin:
    list_display=['id','username','type','content','create_time','is_deleted']

xadmin.site.register(Feedback,FeedbackAdmin)