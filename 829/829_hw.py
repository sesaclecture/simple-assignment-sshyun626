import streamlit as st
import numpy as np
from datetime import datetime

st.title('🚗 Hello Parking')

# 전역 변수 (Streamlit에서는 session_state에 저장해야 유지됨)
if "parking" not in st.session_state:
    st.session_state.parking = np.zeros((2,10))
if "parking_log" not in st.session_state:
    st.session_state.parking_log = {}

discount = {
    "1234":30,
    "1409":50
}

def show_parking():
    park2 = np.where(st.session_state.parking == 0, "[ ]", "[X]")
    st.write("       A   B   C   D   E   F   G   H   I   J")
    floor = 2
    for pa in reversed(park2):
        st.write(f"{floor}층 | " + "  ".join(pa))
        floor -= 1

def car_in(car_num, tar_floor, tar_loc):
    idx_fl = tar_floor - 1
    idx_loc = ord(tar_loc) - 65
    if st.session_state.parking[idx_fl][idx_loc] == 1:
        st.warning("이미 주차된 자리입니다.")
        return
    st.session_state.parking[idx_fl][idx_loc] = 1
    st.session_state.parking_log[car_num] = [(idx_fl, idx_loc), datetime.now(), 0]
    st.success(f"{car_num} 차량이 {tar_floor}층 {tar_loc} 구역에 입차되었습니다.")

def car_out(car_num):
    if car_num not in st.session_state.parking_log:
        st.error("입차 기록이 없습니다.")
        return

    time_out = datetime.now()
    st.session_state.parking_log[car_num][2] = time_out
    time = time_out - st.session_state.parking_log[car_num][1]

    idx_fl, idx_loc = st.session_state.parking_log[car_num][0]
    st.write(f"========={car_num} 출차 정보=========")
    st.write(f"주차 위치 | {idx_fl+1}층 {chr(idx_loc+65)}")
    st.write(f"주차 시간 | {time}")

    # 요금 계산
    if car_num in discount:
        cost = 50*np.ceil(time.seconds//60/10)*10*(100-discount[car_num])/100
        st.write(f"주차 요금 | {int(cost)}원 ({discount[car_num]}% 할인)")
    else:
        cost = 50*np.ceil(time.seconds//60/10)*10
        st.write(f"주차 요금 | {int(cost)}원")

    st.session_state.parking[idx_fl][idx_loc] = 0
    st.success(f"{car_num} 차량 출차 완료!")

# UI 표시
st.subheader("📍 주차 현황")
show_parking()

st.subheader("🚘 차량 입차")
car_num_in = st.text_input("입차 차량 번호")
tar_floor = st.selectbox("층 선택", [1,2])
tar_loc = st.selectbox("자리 선택", list("ABCDEFGHIJ"))
if st.button("입차"):
    if car_num_in:
        car_in(car_num_in, tar_floor, tar_loc)

st.subheader("🚙 차량 출차")
car_num_out = st.text_input("출차 차량 번호")
if st.button("출차"):
    if car_num_out:
        car_out(car_num_out)