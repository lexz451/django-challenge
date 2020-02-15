from rest_framework import mixins, viewsets, views
from rest_framework.response import Response

from . import models
from . import serializers


class AccountViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
        API endpoint that allows accounts to be viewed.

        list:
        Return all the accounts available.

        create:
        Create an account.

        retrieve:
        Return a given account.
    """
    model = models.Account
    serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()


class FizzBuzzView(views.APIView):

    @staticmethod
    def fizz_buzz_program(x):
        return ", ".join(["Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0) or str(i) for i in range(1, x + 1)])

    def get(self, request):
        x = 100
        param = request.query_params.get('x', None)
        if param:
            try:
                x = int(param)
            except ValueError:
                return Response({"error": "Invalid query param"}, status=500)
        result = self.fizz_buzz_program(x)
        return Response({"x": x, "fizzbuzz": result})
