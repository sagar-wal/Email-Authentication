from django.contrib.auth.tokens import PasswordResetTokenGenerator
#from django.utils import six
#from .models.MyAppUser import user #added here
import six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
        #return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.username))
account_activation_token = TokenGenerator()
print(account_activation_token)

