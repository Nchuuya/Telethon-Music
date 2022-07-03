import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "8714251"))
    API_HASH = os.environ.get("API_HASH", "50c97a11b622575c5b9441b1062f601a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5276474965:AAFGJNgQEWJH1qQ8RlHBNAM9e3aJH7ke18c")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJ8Bu3A8QnSlHbodSoqdBD8GytgPYF5s-wZNtQWsYieJ_cjHbf6c-swWxCXopfW9ppLt1Lfl3FRCJQYc1VCWIkbt4XZjX98j55AAO5d4X84fbJTExlYHlOL9baZdPUShcV6YUWnpvbMWYJvWLJxViBrpFnhQqJqA4p8H-7VruKv_Fv_s-BITFAI-8cAhses5I_PK_rOZbvTWh7l7yW7bnTK1qsmpMR71kmiOJ8G5SqJ6wmygVyBPkTcyPScRLRepNACgtDty4nyPDenoYESQyXD_UlPCWYQfuSALMaOsrBmeV48jOoWGCtPuhAidCqAexU0wrLvIesRZ5LZM8FJAqgGZE2o=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "BoaHancock_Robot")
    SUPPORT = os.environ.get("SUPPORT", "boahancock_support")
    CHANNEL = os.environ.get("CHANNEL", "boa_updates")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6435225"))
