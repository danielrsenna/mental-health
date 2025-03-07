import os

import dotenv


dotenv.load_dotenv()


def get_feature_flags():
    features = os.environ.get('MENTAL_HEALTH_FEATURE_FLAGS', '').split(',')
    features = set(map(str.strip, features))
    return features


class FeatureFlags:

    FEATURES = get_feature_flags()

    @classmethod
    def is_message_encryption_enabled(cls):
        return 'encrypt_messages' in cls.FEATURES
