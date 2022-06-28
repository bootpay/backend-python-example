
from bootpay_backend import BootpayBackend
import time
import uuid 
import datetime

bootpay = BootpayBackend('5b8f6a4d396fa665fdc2b5ea', 'rm6EYECr6aroQVG2ntW0A6LpWnkTgP4uQ3H18sDDUYw=')


# 1. (부트페이 통신을 위한) 토큰 발급
def get_token():
    token = bootpay.get_access_token() 
    if 'error_code' not in token:
        # 토큰 발급 성공 
        print(token)


# 2. 결제 단건 조회 
def get_receipt(): 
    response = bootpay.receipt_payment('62b2c3c2d01c7e001bc20b10')
    print(response)


# 3. 결제 취소 (전액 취소 / 부분 취소)
def cancel():
    response = bootpay.cancel_payment(
        receipt_id='62ba5a3cd01c7e001fb45c46', 
        cancel_id=str(uuid.uuid4()),
        cancel_username='test', 
        cancel_message='test결제 취소'
    )
    print(response)


# 4-1. 빌링키 발급
def get_billing_key():
    response = bootpay.request_subscribe_billing_key(
        pg='나이스페이',
        order_name='테스트결제',
        subscription_id=str(time.time()),
        card_no="5570********1074", # 카드번호 
        card_pw="**", # 카드 비밀번호 2자리 
        card_identity_no="******", # 카드 소주 생년월일 
        card_expire_year="**", # 카드 유효기간 년 2자리 
        card_expire_month="**",  # 카드 유효기간 월 2자리 

    )
    print(response)

# 4-2. 발급된 빌링키로 결제 승인 요청
def subscribe_billing():
    response = bootpay.request_subscribe_card_payment(
        billing_key='62b2c3cfd01c7e001cc20a84',
        order_name='테스트결제',
        order_id=str(time.time()),
        price=100,
        user={
            "phone": '01000000000',
            "username": '홍길동',
            "email": 'test@bootpay.co.kr'
        }
    )
    print(response)

# 4-3. 발급된 빌링키로 결제 예약 요청
def subscribe_billing_reserve():
    response = bootpay.subscribe_payment_reserve(
        billing_key='[ 빌링키 ]',
        order_name='테스트결제',
        order_id=str(time.time()),
        price=1000,
        user={
            "phone": '01000000000',
            "username": '홍길동',
            "email": 'test@bootpay.co.kr'
        },
        reserve_execute_at=(datetime.datetime.now() + datetime.timedelta(seconds=5)).astimezone().strftime(
            '%Y-%m-%dT%H:%M:%S%z')
    )
    print(response)

# 4-4. 발급된 빌링키로 결제 예약 - 취소 요청
def subscribe_billing_reserve_cancel():
    result = bootpay.cancel_subscribe_reserve(
        '612debc70d681b0039e6133d'
    )
    print(result)

# 4-5. 빌링키 삭제
def destroy_subscribe_billing_key():
    response = bootpay.destroy_billing_key(
        billing_key='62b2c3cfd01c7e001cc20a85',
    )
    print(response)

# 4-6. 빌링키 조회
def lookup_billing_key():    
    response = bootpay.lookup_subscribe_billing_key('62b2c3c2d01c7e001bc20b10')
    print(response)

# 5. (생체인증, 비밀번호 결제를 위한) 구매자 토큰 발급
def get_user_token():
    result = bootpay.request_user_token({
        'user_id': '12341-234',
        'email': 'test@email.com',
        'name': '홍길동',
        'gender': '1',
        'birth': '901014',
        'phone': '01012341234'
    })
    print(result)

# 6. 서버 승인 요청
def server_confirm():
    result = bootpay.confirm_payment(
        receipt_id='612df0250d681b001de61de6'
    )
    print(result)

# 7. 본인 인증 결과 조회
def certificate():
    result = bootpay.certificate(
        receipt_id='612df0250d681b001de61de6'
    )
    print(result)

# 8. (에스크로 이용시) PG사로 배송정보 보내기
def shipping_start():
    response = bootpay.shipping_start(
        receipt_id="62a946aad01c7e001b7dc20b",
        tracking_number='3989838',
        delivery_corp='CJ대한통운',
        user={
            "phone": '01000000000',
            "username": '홍길동',
            "address": "서울특별시 종로구",
            "zipcode": "039899"
        }
    )
    print(response)


# 실행 부분
get_token()
get_receipt()
cancel()
get_billing_key()
subscribe_billing()
subscribe_billing_reserve()
subscribe_billing_reserve_cancel()
destroy_subscribe_billing_key()
lookup_billing_key()
get_user_token()
server_confirm() 
certificate()
shipping_start()