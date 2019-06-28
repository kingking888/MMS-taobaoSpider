# 自定义Error
class NoShopException(Exception):  # 无相关商品Error

    pass


class LittleResultException(Exception):    # 相关商品太少Error

    pass


class NetWorkError(Exception):    # 网络较差Error

    pass
