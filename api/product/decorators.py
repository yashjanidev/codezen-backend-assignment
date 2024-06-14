from functools import wraps
from rest_framework.response import Response
from rest_framework import status


def customer_only(view_func):
    @wraps(view_func)
    def _wrapped_view(viewset, request, *args, **kwargs):
        user = request.user
        if not user.is_staff and not hasattr(user, 'customer'):
            return Response({'detail': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        return view_func(viewset, request, *args, **kwargs)
    return _wrapped_view
