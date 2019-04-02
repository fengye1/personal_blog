from graphene import Interface, String, Boolean, Int


class MutationResponse(Interface):
    code = Int(required=True, description="状态码", default_value="200")
    success = Boolean(required=True, description="操作成功或失败", default_value=True)
    message = String(required=True, description="服务器信息", default_value="操作成功")





