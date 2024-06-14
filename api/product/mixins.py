from .models import PlatformApiCall


class PlatformApiCallMixin:
    def perform_create(self, serializer):
        instance = serializer.save()
        PlatformApiCall.objects.create(
            user=self.request.user,
            requested_url=self.request.build_absolute_uri(),
            requested_data=self.request.data,
            response_data={'id': instance.id}
        )
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        PlatformApiCall.objects.create(
            user=self.request.user,
            requested_url=self.request.build_absolute_uri(),
            requested_data=self.request.data,
            response_data={'id': instance.id}
        )
        return instance

    def perform_destroy(self, instance):
        PlatformApiCall.objects.create(
            user=self.request.user,
            requested_url=self.request.build_absolute_uri(),
            requested_data=self.request.data,
            response_data={'status': 'deleted'}
        )
        return super().perform_destroy(instance)
