from diaries.DiarySample import DiarySample
from diaries.TsukamotoDiary import TsukamotoDiary
from diaries.ShimokawaDiary import ShimokawaDiary
from diaries.GotoDiary import GotoDiary
from diaries.KinoshitaDiary import KinoshitaDiary
from diaries.YamakadoDiary import YamakadoDiary
from diaries.YuichiDiary import Yuichisample
from diaries.HazukaDiary import HazukaDiary
from diaries.OtaDiary import OtaDiary
# ↓のリストには、メンバーの各日記が格納されます。

diaries = [
    DiarySample(), 
    TsukamotoDiary(),
    ShimokawaDiary(),
    GotoDiary(),
    KinoshitaDiary(),
    YamakadoDiary(),
    Yuichisample(),
    HazukaDiary(),
    OtaDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()