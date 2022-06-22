import json
import os.path


def raceCreate():
    global sp_start, mp_start, ip_start, pp_start, ap_start, bp_start, cp_start, lp_start, fp_start, sp_max, mp_max, ip_max, pp_max, ap_max, fp_max, lp_max, cp_max, bp_max, fire_res_start, stab_res_start, cut_res_start, crush_res_start, curse_res_start, holy_res_start, lightning_res_start, dirt_res_start, wind_res_start, water_res_start, fire_access_start, water_access_start, wind_access_start, dirt_access_start, lightning_access_start, holy_access_start, curse_access_start, bleed_access_start, nature_access_start, mental_access_start, twohanded_access_start, polearm_access_start, onehanded_access_start, stabbing_access_start, cutting_access_start, crushing_access_start, small_arms_access_start, shields_access_start, gloves_status_start, shoes_status_start, chest_status_start, helmet_status_start, item_slot_start
    check_file = os.path.exists('Races')
    if check_file:
        print("Введите название расы")
        race_name = input()
        race_name.lower()
        if os.path.exists('Races/' + race_name):
            print("Данная раса уже существует")
            raceCreate()
        else:
            print("Введите начальные и конечные очки расы: ")
            print("Стамина")
            sp_start = input()
            sp_max = input()
            print("Колдовство")
            mp_start = input()
            mp_max = input()
            print("Интелект")
            ip_start = input()
            ip_max = input()
            print("Сила")
            pp_start = input()
            pp_max = input()
            print("Ловкость")
            ap_start = input()
            ap_max = input()
            print("Вера")
            fp_start = input()
            fp_max = input()
            print("Удача")
            lp_start = input()
            lp_max = input()
            print("Харизма")
            cp_start = input()
            cp_max = input()
            print("Рассудок")
            bp_start = input()
            bp_max = input()

            print("Введите стартовые сопративления расы к различным типам урона: ")
            print("Сопративление к огню")
            fire_res_start = input()
            print("Сопративление к воде")
            water_res_start = input()
            print("Сопративление к воздху")
            wind_res_start = input()
            print("Сопративление к земле")
            dirt_res_start = input()
            print("Сопративление к молниям")
            lightning_res_start = input()
            print("Сопративление к свету")
            holy_res_start = input()
            print("Сопративление ко тьме")
            curse_res_start = input()
            print("Сопративление к протыканию")
            cut_res_start = input()
            print("Сопративление к порезам")
            stab_res_start = input()
            print("Сопративление к дроблению")
            crush_res_start = input()

            print("Введите стартовые очки умений: ")
            print("Пирокинектика")
            fire_access_start = input()
            print("Гидрософистика")
            water_access_start = input()
            print("Аэрософистика")
            wind_access_start = input()
            print("Геомантия")
            dirt_access_start = input()
            print("Киловактика")
            lightning_access_start = input()
            print("Элафриситка")
            holy_access_start = input()
            print("Катифристика")
            curse_access_start = input()
            print("Гематомантия")
            bleed_access_start = input()
            print("Ботаника")
            nature_access_start = input()
            print("Псифистика")
            mental_access_start = input()
            print("Владение навыками Колющего оружия")
            twohanded_access_start = input()
            print("Владение навыками Режущего оружия")
            polearm_access_start = input()
            print("Владение навыками Дробящего оружия")
            onehanded_access_start = input()
            print("Владение навыками Двуручного оружия")
            stabbing_access_start = input()
            print("Владение навыками Древкового оружия")
            cutting_access_start = input()
            print("Владение навыками Одноручного оружия")
            crushing_access_start = input()
            print("Владение навыками Стрелкового оружия")
            small_arms_access_start = input()
            print("Владение навыками щитов")
            shields_access_start = input()

            print("Введите стартовые очки экипировки: ")
            print("Шлем")
            helmet_status_start = input()
            print("Нагрудник")
            chest_status_start = input()
            print("Ботинки")
            shoes_status_start = input()
            print("Наручи")
            gloves_status_start = input()
            print("Предметы экипировки")
            item_slot_start = input()
        race = {
            'RACE_NAME': race_name,
            'POINTS':
                {
                    'START_POINTS':
                        {
                            'SP_START': sp_start,
                            'MP_START': mp_start,
                            'IP_START': ip_start,
                            'PP_START': pp_start,
                            'AP_START': ap_start,
                            'FP_START': fp_start,
                            'LP_START': lp_start,
                            'CP_START': cp_start,
                            'BT_START': bp_start
                        },
                    'MAX_POINTS':
                        {
                            'SP_MAX': sp_max,
                            'MP_MAX': mp_max,
                            'IP_MAX': ip_max,
                            'PP_MAX': pp_max,
                            'AP_MAX': ap_max,
                            'FP_MAX': fp_max,
                            'LP_MAX': lp_max,
                            'CP_MAX': cp_max,
                            'BT_MAX': bp_max
                        }
                },
            'RESISTANCES':
                {
                    'FIRE_RES_START': fire_res_start,
                    'WATER_RES_START': water_res_start,
                    'WIND_RES_START': wind_res_start,
                    'DIRT_RES_START': dirt_res_start,
                    'LIGHTNING_RES_START': lightning_res_start,
                    'HOLY_RES_START': holy_res_start,
                    'CURSE_RES_START': curse_res_start,
                    'CRUSH_RES_START': crush_res_start,
                    'CUT_RES_START': cut_res_start,
                    'STAB_RES_START': stab_res_start
                },
            'PERMISSIONS':
                {
                    'FIRE_ACCESS_START': fire_access_start,
                    'WATER_ACCESS_START': water_access_start,
                    'WIND_ACCESS_START': wind_access_start,
                    'DIRT_ACCESS_START': dirt_access_start,
                    'LIGHTNING_ACCESS_START': lightning_access_start,
                    'HOLY_ACCESS_START': holy_access_start,
                    'CURSE_ACCESS_START': curse_access_start,
                    'BLEED_ACCESS_START': bleed_access_start,
                    'NATURE_ACCESS_START': nature_access_start,
                    'MENTAL_ACCESS_START': mental_access_start,
                    'TWOHANDED_ACCESS_START': twohanded_access_start,
                    'POLEARM_ACCESS_START': polearm_access_start,
                    'ONEHANDED_ACCESS_START': onehanded_access_start,
                    'STABBING_ACCESS_START': stabbing_access_start,
                    'CUTTING_ACCESS_START': cutting_access_start,
                    'CRUSHING_ACCESS_START': crushing_access_start,
                    'SMALL_ARMS_ACCESS_START': small_arms_access_start,
                    'SHIELDS_ACCESS_START': shields_access_start
                },
            'EQUIPMENT':
                {
                    'HELMET_STATUS_START': helmet_status_start,
                    'CHEST_STATUS_START': chest_status_start,
                    'SHOES_STATUS_START': shoes_status_start,
                    'GLOVES_STATUS_START': gloves_status_start,
                    'ITEM_SLOT_START': item_slot_start,
                }
        }
        with open("Races/"+race_name.lower()+".json", "w") as json_file:
            json.dump(race, json_file)


raceCreate()
