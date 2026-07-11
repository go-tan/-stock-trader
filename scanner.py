import time

MIN_CHANGE = 3.0

def scan():
    print("="*40)
    print("日本株スキャナー")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("="*40)
    stocks=[
        {"code":"7011","name":"三菱重工","change":4.2},
        {"code":"8306","name":"三菱UFJ","change":3.5},
        {"code":"7203","name":"トヨタ","change":1.1},
    ]
    print("条件: 値上がり率3%以上\n")
    for s in stocks:
        if s["change"]>=MIN_CHANGE:
            print(f'{s["code"]} {s["name"]} {s["change"]}%')

if __name__=="__main__":
    scan()
