from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(32) NOT NULL,
    "age" SMALLINT NOT NULL,
    "bio" VARCHAR(200) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztVm1v2jAQ/itRPnVSV5XwVu1bypjKxMtU0m1qVUUmNsHCsdPEWYuq/PfZToJDgAykSQ"
    "Npn8DPPY7vnjvf+d0MGEQkvnqIUWR+Mt5NCgIk/mzgl4YJwlCjEuBgRhQxEQyFgFnMI+Bx"
    "Ac4BiZGAIIq9CIccMypQmhAiQeYJIqa+hhKKXxLkcuYjvlCOPD0LGFOI3lBcLMOlO8eIwA"
    "0/MZRnK9zlq1BhA8q/KKI8beZ6jCQB1eRwxReMrtmYcon6iKIIcCQ/z6NEui+9y8MsIso8"
    "1ZTMxdIeiOYgIbwU7oEaeIxK/YQ3sQrQl6d8tBqtbuum2WndCIryZI100yw8HXu2USkwds"
    "xU2QEHGUPJqHXzIiSDdQHf1u+zsHAcoN0ibu6siAnzrVfFn6q0hZB12haAFlcX1F9SV8QA"
    "J5Ss8sTVSOkMRv2pY4++yUiCOH4hSiLb6UuLpdBVBb3ofJA4E9chuyTrjxg/Bs6dIZfG42"
    "TcVwqymPuROlHznEdT+gQSzlzKXl0ASzVWoIUwgqkTq363UtpbgGh3Ogt+JZFCrRNNXQDe"
    "XIKozxdi2bRqUvfdvu/d2fcXTauSjnFusZQp3dAP+DvkmwaAkL1tJd/y575yIgpmraVpdT"
    "vrriIXdQ1lOrKHw6KraLFmmB1Tazn9PEvNur4+oNYEa2+xKVuaylk2X5a6sgRmwFu+ggi6"
    "WxZmsX3cbVNgBVUEUFGfMA9SRpCPdhtF2FvsGvq5pXbsA835P/fPaO7/Eq816dIRt7a05U"
    "xvbrt9yM1tt/ffXGmrzAlxNY4QMaefp4CNg1pfo6b1NbLWVxZQnMgR3fH8/DqdjPc8PfWW"
    "ipAPVAT4BLHHLw2CY/58mrLWqCij3nhiFuJdjOyfVV17w8lt9e0oP3D7r8dL+ht1cI12"
)
