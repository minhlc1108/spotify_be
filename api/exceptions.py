from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(response.data, list):
            # Trường hợp message là một danh sách lỗi
            message = response.data[0]
        elif isinstance(response.data, dict):
            # Lấy thông báo lỗi đầu tiên
            key = next(iter(response.data))
            val = response.data[key]
            if isinstance(val, list):
                message = val[0]
            else:
                message = val
        else:
            message = "Đã xảy ra lỗi không xác định."

        response.data = {"message": message}

    return response
