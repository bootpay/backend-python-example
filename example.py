from bootpay import Bootpay
import time

rest_application_id = '5b8f6a4d396fa665fdc2b5ea'
rest_private_key = 'rm6EYECr6aroQVG2ntW0A6LpWnkTgP4uQ3H18sDDUYw='
bootpay = Bootpay(rest_application_id, rest_private_key)


# 1. 토큰 발급
def get_token():
    result = bootpay.get_access_token()
    print(result)
    print(result['data']['token'])


# 2. 결제 검증
def verification():
    receipt_id = '612df0250d681b001de61de6'
    result = bootpay.verify(receipt_id)
    print(result)


# 3. 결제 취소 (전액 취소 / 부분 취소)
def cancel():
    receipt_id = '612df0250d681b001de61de6'
    result = bootpay.cancel(
        receipt_id,
    )
    print(result)


# 4. 빌링키 발급
def get_billing_key():
    result = bootpay.get_subscribe_billing_key(
        'nicepay',
        '1234-1234-1234',
        '30일 결제권',
        '[ 카드 번호 ]',
        '[ 카드 비밀번호 앞자리 2개 ]',
        '[ 카드 만료 연도 2자리 ]',
        '[ 카드 만료 월 2자리 ]',
        '[ 카드 소유주 생년월일 혹은 사업자 등록번호 ]',
        None,
        {
            'subscribe_test_payment': 1
        }
    )
    print(result)

# 4-1. 발급된 빌링키로 결제 승인 요청
def subscribe_billing():
    billing_key = '612deb53019943001fb52312'
    result = bootpay.subscribe_billing(
        billing_key,
        '정기 결제 테스트 아이템',
        3000,
        '12345',
        [],
        {'username': 'test'}
    )
    print(result)

# 4-2. 발급된 빌링키로 결제 예약 요청
def subscribe_billing_reserve():
    billing_key = '612deb53019943001fb52312'
    result = bootpay.subscribe_billing_reserve(
        billing_key,
        '정기 결제 테스트 아이템',
        3000,
        '12345',
        time.time() + 10

    )
    print(result)

# 4-2-1. 발급된 빌링키로 결제 예약 - 취소 요청
def subscribe_billing_reserve_cancel():
    reserve_id = '612debc70d681b0039e6133d'
    result = bootpay.subscribe_billing_reserve_cancel(
        reserve_id
    )
    print(result)

# 4-3. 빌링키 삭제
def destroy_subscribe_billing_key():
    billing_key = '612debc70d681b0039e6133d'
    result = bootpay.destroy_subscribe_billing_key(
        billing_key
    )
    print(result)

# 5. (부트페이 단독 - 간편결제창, 생체인증 기반의 사용자를 위한) 사용자 토큰 발급
def get_user_token():
    result = bootpay.get_user_token({
        'user_id': '12341-234',
        'email': 'test@email.com',
        'name': '홍길동',
        'gender': '1',
        'birth': '901014',
        'phone': '01012341234'
    })
    print(result)

# 6. 결제링크 생성
def request_payment():
    result = bootpay.request_payment({
        'pg': 'kcp',
        'method': 'card',
        'order_id': '1234-1234',
        'price': 1000,
        'name': '테스트 부트페이 상품',
        'return_url': 'https://www.yourdomain.com/callback',
        'extra': {
            'expire': 30
        }
    })
    print(result)

# 7. 서버 승인 요청
def server_submit():
    result = bootpay.submit('')
    print(result)

# 8. 본인 인증 결과 검증
def certificate():
    receipt_id = '612df0250d681b001de61de6'
    result = bootpay.certificate(receipt_id)
    print(result)


# 실행 부분
get_token()
verification()
cancel()
get_billing_key()
subscribe_billing()
subscribe_billing_reserve()
subscribe_billing_reserve_cancel()
destroy_subscribe_billing_key()
get_user_token()
request_payment()
server_submit()
certificate()