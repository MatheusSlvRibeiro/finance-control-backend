from drf_yasg.utils import swagger_auto_schema


def auto_swagger_viewset(tags):
    """
    Helper para aplicar decoradores swagger automaticamente em um ViewSet.
    
    Usage:
        class MyViewSet(viewsets.ModelViewSet):
            # ... configurações normais
            
            # No final da classe, adicione:
            locals().update(auto_swagger_viewset(['🏷️ Minha Tag']))
    """
    methods = {
        'list': f'Lista todos os itens',
        'create': f'Cria um novo item',
        'retrieve': f'Recupera detalhes de um item',
        'update': f'Atualiza um item',
        'partial_update': f'Atualiza parcialmente um item',
        'destroy': f'Remove um item'
    }
    
    decorated_methods = {}
    
    for method_name, description in methods.items():
        def create_method(method_name, description):
            @swagger_auto_schema(tags=tags, operation_description=description)
            def method(self, request, *args, **kwargs):
                return getattr(super(self.__class__, self), method_name)(request, *args, **kwargs)
            return method
        
        decorated_methods[method_name] = create_method(method_name, description)
    
    return decorated_methods


def swagger_viewset_methods(tags, entity_name=None):
    """
    Helper mais específico que gera métodos com descrições personalizadas.
    
    Usage:
        class HoldingViewSet(viewsets.ModelViewSet):
            # ... configurações normais
            
            # No final da classe:
            locals().update(swagger_viewset_methods(HOLDING_TAGS, 'holding'))
    """
    entity = entity_name or 'item'
    
    methods_config = {
        'list': f'Lista todas as {entity}s',
        'create': f'Cria uma nova {entity}',
        'retrieve': f'Recupera detalhes de uma {entity}',
        'update': f'Atualiza uma {entity}',
        'partial_update': f'Atualiza parcialmente uma {entity}',
        'destroy': f'Remove uma {entity}'
    }
    
    decorated_methods = {}
    
    for method_name, description in methods_config.items():
        def create_method(method_name, description):
            @swagger_auto_schema(tags=tags, operation_description=description)
            def method(self, request, *args, **kwargs):
                return getattr(super(self.__class__, self), method_name)(request, *args, **kwargs)
            return method
        
        decorated_methods[method_name] = create_method(method_name, description)
    
    return decorated_methods
