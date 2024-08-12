class TitleMixin(object):
    title = None
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title'] = self.get_title()
        return context
    def get_title(self):
        return self.title
    
class LinkMixin(object):
    link = None
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['link'] = self.get_link()
        return context
    def get_link(self):
        return self.link

class StyleMix(object):
    stylesheet = None 
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['stylesheet'] = self.get_stylesheet()
        return context
    def get_stylesheet(self):
        return self.stylesheet
    