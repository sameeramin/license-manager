"""
URL definitions for license manager API version 1.

The use of `NestedSimpleRouter` below allows us to defined
nested routes backed by the `SubscriptionViewSet`.  That is:

/api/v1/subscriptions/{subscription_uuid}/licenses/
/api/v1/subscriptions/{subscription_uuid}/licenses/{license_uuid}/
"""
from rest_framework_nested import routers

from license_manager.apps.api.v1 import views


app_name = 'v1'


class NestedMixin(routers.NestedMixin):
    """
    This is a hack to work around a shortcoming of the rest_framework_nested
    `NestedMixin` class: https://github.com/alanjds/drf-nested-routers/issues/147

    Without this trickery, you can't tell `NestedMixin` to just use
    the `lookup_field` or `lookup_url_kwarg` of the router's viewset as the
    lookup URL kwarg of a nested router - it will *always* try to build its
    own, non-empty default if not provided, and will insist on appending a "_"
    if you provide a non-empty value.  The properties below trick this base
    class's __init__() method into not doing anything during mutation,
    but returning an empty string when `nest_prefix` is read.  The `nest_prefix`
    is used as a prefix of either the ViewSets `lookup_url` or `lookup_url_kwarg`
    field when building the lookup regular expression's name.
    """
    @property
    def nest_prefix(self):
        return ""

    @nest_prefix.setter
    def nest_prefix(self, value):
        pass

    def check_valid_name(self, value):
        return True


class NestedSimpleRouter(NestedMixin, routers.SimpleRouter):
    """
    Same as `rest_framework_nested.routers.NestedSimpleRouter`, only
    with the custom `NestedMixin` defined above.
    """


router = routers.SimpleRouter()
router.register(
    prefix=r'subscriptions',
    viewset=views.SubscriptionViewSet,
    basename='subscriptions',
)

subscription_router = NestedSimpleRouter(
    parent_router=router,
    parent_prefix=r'subscriptions',
)
subscription_router.register(
    r'licenses',
    views.LicenseViewSet,
    basename='licenses',
)

urlpatterns = router.urls + subscription_router.urls
