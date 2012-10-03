from errormator_client.utils import import_module, deco_func_or_method
from errormator_client.timing import time_trace

def add_timing(min_duration=0.05):
    module = import_module('django')
    if not module:
        return
   
    from django import template
    
    def gather_template(template, *args, **kwargs):
        return {'type':'template',
                'statement':'Template.render',
                'parameters':template.name}
    
    if hasattr(template.Template, 'render'):
        deco_func_or_method(template, 'Template.render', time_trace,
                          gather_template, min_duration)
    elif hasattr(template.Template, '_render'):
        deco_func_or_method(template, 'Template._render', time_trace,
                          gather_template, min_duration)
