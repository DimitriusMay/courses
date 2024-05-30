from tastypie.authentication import ApiKeyAuthentication


# Аутентификация для методов(по api-ключу)
class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        # метод get не будет требовать аутентификации
        if request.method == "GET":
            return True
        # остальные методы будут требовать аутентификацию
        return super().is_authenticated(request, **kwargs)