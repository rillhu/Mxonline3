from .models import Course, Lesson, Video, CourseResource,BannerCourse
import xadmin

# Course的admin管理器


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail',
                    'degree',
                    'learn_times',
                    'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']
    # 富文本
    style_fields = {"detail": "ueditor"}


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']


class BannerCourseAdmin(object):
    '''轮播课程'''

    list_display = [ 'name','desc','detail','degree','learn_times','students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [ 'name','desc','detail','degree','learn_times','students']
    #model_icon = 'fa fa-book'
    #ordering = ['-click_nums']
    #readonly_fields = ['click_nums']
    #exclude = ['fav_nums']
    #inlines = [Lesson,CourseResource]

    def queryset(self):
        #重载queryset方法，来过滤出我们想要的数据的
        qs = super(BannerCourseAdmin, self).queryset()
        #只显示is_banner=True的课程
        qs = qs.filter(is_banner=True)
        return qs

# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)