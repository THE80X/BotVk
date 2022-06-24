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
        with open("Races/" + race_name.lower() + ".json", "w") as json_file:
            json.dump(race, json_file)


def thingCreate():
    check_file = os.path.exists('Things')
    if check_file:
        print("Введите название артефакта")
        thing_name = input()
        thing_name.lower()
        if os.path.exists('Things/' + thing_name):
            print("Данный артефакт уже существует")
            thingCreate()
        else:
            print("\n" + "Введите прочность артефакта: нынешнюю и максимальную ")
            durability_now = input()
            durability_max = input()
            print("Ввердите вес артефакта: ")
            weight = input()
            print("Введите стоимость купли и продажи артефакта: ")
            cost_thing_buy = input()
            cost_thing_sell = input()

            print("\n" + "Введите номер требования для экипировки артефакта")
            id_permission_equip_to = int(input())
            idk_1 = {
                str(id_permission_equip_to): "EQUIP_TO"
            }

            print("\n" + "Введите требования для экипировки артефакта связанные с очками: ")
            print("Стамина")
            sp_equip_to = input()
            print("Колдовство")
            mp_equip_to = input()
            print("Интелект")
            ip_equip_to = input()
            print("Сила")
            pp_equip_to = input()
            print("Ловкость")
            ap_equip_to = input()
            print("Вера")
            fp_equip_to = input()
            print("Удача")
            lp_equip_to = input()
            print("Харизма")
            cp_equip_to = input()
            print("Рассудок")
            bp_equip_to = input()

            print("\n" + "Введите требования для экипировки артефакта связанные с очками умений: ")
            print("Пирокинектика")
            fire_access_equip_to_thing = input()
            print("Гидрософистика")
            water_access_equip_to_thing = input()
            print("Аэрософистика")
            wind_access_equip_to_thing = input()
            print("Геомантия")
            dirt_access_equip_to_thing = input()
            print("Киловактика")
            lightning_access_equip_to_thing = input()
            print("Элафриситка")
            holy_access_equip_to_thing = input()
            print("Катифристика")
            curse_access_equip_to_thing = input()
            print("Гематомантия")
            bleed_access_equip_to_thing = input()
            print("Ботаника")
            nature_access_equip_to_thing = input()
            print("Псифистика")
            mental_access_equip_to_thing = input()
            print("Владение навыками Колющего оружия")
            twohanded_access_equip_to_thing = input()
            print("Владение навыками Режущего оружия")
            polearm_access_equip_to_thing = input()
            print("Владение навыками Дробящего оружия")
            onehanded_access_equip_to_thing = input()
            print("Владение навыками Двуручного оружия")
            stabbing_access_equip_to_thing = input()
            print("Владение навыками Древкового оружия")
            cutting_access_equip_to_thing = input()
            print("Владение навыками Одноручного оружия")
            crushing_access_equip_to_thing = input()
            print("Владение навыками Стрелкового оружия")
            small_arms_access_equip_to_thing = input()
            print("Владение навыками щитов")
            shields_access_equip_to_thing = input()

            print("\n" + "Введите очки экипировки, занимаемые артефактом: ")
            print("Шлем")
            helmet_status_equip_to_thing = input()
            print("Нагрудник")
            chest_status_equip_to_thing = input()
            print("Ботинки")
            shoes_status_equip_to_thing = input()
            print("Наручи")
            gloves_status_equip_to_thing = input()
            print("Предметы экипировки")
            item_slot_equip_to_thing = input()

            print("\n" + "Введите номер требования для экипировки и использования артефакта:")
            id_permission_use_to = int(input())
            idk_2 = {
                str(id_permission_use_to): "USE_TO"
            }

            print("\n" + "Введите требования для экипировки и использования артефакта связанные с очками: ")
            print("Стамина")
            sp_use_to = input()
            print("Колдовство")
            mp_use_to = input()
            print("Интелект")
            ip_use_to = input()
            print("Сила")
            pp_use_to = input()
            print("Ловкость")
            ap_use_to = input()
            print("Вера")
            fp_use_to = input()
            print("Удача")
            lp_use_to = input()
            print("Харизма")
            cp_use_to = input()
            print("Рассудок")
            bp_use_to = input()

            print("\n" + "Введите требования для экипировки и использования артефакта связанные с очками умений: ")
            print("Пирокинектика")
            fire_access_use_to_thing = input()
            print("Гидрософистика")
            water_access_use_to_thing = input()
            print("Аэрософистика")
            wind_access_use_to_thing = input()
            print("Геомантия")
            dirt_access_use_to_thing = input()
            print("Киловактика")
            lightning_access_use_to_thing = input()
            print("Элафриситка")
            holy_access_use_to_thing = input()
            print("Катифристика")
            curse_access_use_to_thing = input()
            print("Гематомантия")
            bleed_access_use_to_thing = input()
            print("Ботаника")
            nature_access_use_to_thing = input()
            print("Псифистика")
            mental_access_use_to_thing = input()
            print("Владение навыками Колющего оружия")
            twohanded_access_use_to_thing = input()
            print("Владение навыками Режущего оружия")
            polearm_access_use_to_thing = input()
            print("Владение навыками Дробящего оружия")
            onehanded_access_use_to_thing = input()
            print("Владение навыками Двуручного оружия")
            stabbing_access_use_to_thing = input()
            print("Владение навыками Древкового оружия")
            cutting_access_use_to_thing = input()
            print("Владение навыками Одноручного оружия")
            crushing_access_use_to_thing = input()
            print("Владение навыками Стрелкового оружия")
            small_arms_access_use_to_thing = input()
            print("Владение навыками щитов")
            shields_access_use_to_thing = input()

            print("\n" + "Введите очки экипировки и использования, занимаемые артефактом: ")
            print("Шлем")
            helmet_status_use_to_thing = input()
            print("Нагрудник")
            chest_status_use_to_thing = input()
            print("Ботинки")
            shoes_status_use_to_thing = input()
            print("Наручи")
            gloves_status_use_to_thing = input()
            print("Предметы экипировки")
            item_slot_use_to_thing = input()

            print("Введите число вводимых требований")
            i = int(input())
            list_of_requirements = []
            for z in range(i):
                print("Введите требование " + str(z) + ":")
                permission = int(input())
                list_of_requirements.append(permission)
            print("Введите число необходимых требований для использования особенностей:")
            amount_of_requirements = input()

            print("\n" + "Введите номер награды за экипировку артефакта:")
            id_gives_equip_to = int(input())
            idk_3 = {
                str(id_gives_equip_to): "ABLE_TO_EQUIP"
            }

            print("\n" + "Введите получаемые очки за экипировку артефакта: ")
            print("Стамина")
            sp_gives_equip_to = input()
            print("Колдовство")
            mp_gives_equip_to = input()
            print("Интелект")
            ip_gives_equip_to = input()
            print("Сила")
            pp_gives_equip_to = input()
            print("Ловкость")
            ap_gives_equip_to = input()
            print("Вера")
            fp_gives_equip_to = input()
            print("Удача")
            lp_gives_equip_to = input()
            print("Харизма")
            cp_gives_equip_to = input()
            print("Рассудок")
            bp_gives_equip_to = input()

            print("\n" + "Введите получаемые сопративления к различным типам урона за экипировку артефакта: ")
            print("Сопративление к огню")
            fire_res_gives_equip_to = input()
            print("Сопративление к воде")
            water_res_gives_equip_to = input()
            print("Сопративление к воздху")
            wind_res_gives_equip_to = input()
            print("Сопративление к земле")
            dirt_res_gives_equip_to = input()
            print("Сопративление к молниям")
            lightning_res_gives_equip_to = input()
            print("Сопративление к свету")
            holy_res_gives_equip_to = input()
            print("Сопративление ко тьме")
            curse_res_gives_equip_to = input()
            print("Сопративление к протыканию")
            cut_res_gives_equip_to = input()
            print("Сопративление к порезам")
            stab_res_gives_equip_to = input()
            print("Сопративление к дроблению")
            crush_res_gives_equip_to = input()

            print("\n" + "Введите получаемые очки урона за экипировку артефакта: ")
            print("Дробящий урон")
            crush_damage_gives_equip_to = input()
            print("Разрубающий урон")
            cut_damage_gives_equip_to = input()
            print("Колющий урон")
            stab_damage_gives_equip_to = input()

            print("\n" + "Введите получаемые очки экипировки, занимаемые артефактом: ")
            print("Шлем")
            helmet_status_gives_equip_to_thing = input()
            print("Нагрудник")
            chest_status_gives_equip_to_thing = input()
            print("Ботинки")
            shoes_status_gives_equip_to_thing = input()
            print("Наручи")
            gloves_status_gives_equip_to_thing = input()
            print("Предметы экипировки")
            item_slot_gives_equip_to_thing = input()

            print("\n" + "Введите колличество дающих разрешений, дающего артефактом при экипировке: ")
            i = int(input())
            z = 0
            list_of_permissions_equip_to = []
            for z in range(i):
                print("Введите требование " + str(z) + ":")
                permission = int(input())
                list_of_permissions_equip_to.append(permission)

            print("\n" + "Введите номер награды за экипировку и использование артефакта:")
            id_gives_use_to = int(input())
            idk_4 = {
                str(id_gives_use_to): "ABLE_TO_USE"
            }

            print("\n" + "Введите получаемые очки за экипировку и использование артефакта: ")
            print("Стамина")
            sp_gives_use_to = input()
            print("Колдовство")
            mp_gives_use_to = input()
            print("Интелект")
            ip_gives_use_to = input()
            print("Сила")
            pp_gives_use_to = input()
            print("Ловкость")
            ap_gives_use_to = input()
            print("Вера")
            fp_gives_use_to = input()
            print("Удача")
            lp_gives_use_to = input()
            print("Харизма")
            cp_gives_use_to = input()
            print("Рассудок")
            bp_gives_use_to = input()

            print("\n" + "Введите получаемые сопративления к различным типам урона за экипировку и использование артефакта: ")
            print("Сопративление к огню")
            fire_res_gives_use_to = input()
            print("Сопративление к воде")
            water_res_gives_use_to = input()
            print("Сопративление к воздху")
            wind_res_gives_use_to = input()
            print("Сопративление к земле")
            dirt_res_gives_use_to = input()
            print("Сопративление к молниям")
            lightning_res_gives_use_to = input()
            print("Сопративление к свету")
            holy_res_gives_use_to = input()
            print("Сопративление ко тьме")
            curse_res_gives_use_to = input()
            print("Сопративление к протыканию")
            cut_res_gives_use_to = input()
            print("Сопративление к порезам")
            stab_res_gives_use_to = input()
            print("Сопративление к дроблению")
            crush_res_gives_use_to = input()

            print("\n" + "Введите получаемые очки урона за экипировку и использоваение артефакта: ")
            print("Огненный урон")
            fire_damage_gives_use_to = input()
            print("Водяной урон")
            water_damage_gives_use_to = input()
            print("Воздушный урон")
            wind_damage_gives_use_to = input()
            print("Земляной урон")
            dirt_damage_gives_use_to = input()
            print("Электрический урон")
            lightning_damage_gives_use_to = input()
            print("Светлый урон")
            holy_damage_gives_use_to = input()
            print("Тёмный урон")
            curse_damage_gives_use_to = input()
            print("Дробящий урон")
            crush_damage_gives_use_to = input()
            print("Разрубающий урон")
            cut_damage_gives_use_to = input()
            print("Колющий урон")
            stab_damage_gives_use_to = input()
            print("Чистый урон")
            clear_damage_gives_use_to = input()

            print("\n" + "Введите получаемые очки умений за экипировку и использоваение артефакта: ")
            print("Пирокинектика")
            fire_access_gives_use_to_thing = input()
            print("Гидрософистика")
            water_access_gives_use_to_thing = input()
            print("Аэрософистика")
            wind_access_gives_use_to_thing = input()
            print("Геомантия")
            dirt_access_gives_use_to_thing = input()
            print("Киловактика")
            lightning_access_gives_use_to_thing = input()
            print("Элафриситка")
            holy_access_gives_use_to_thing = input()
            print("Катифристика")
            curse_access_gives_use_to_thing = input()
            print("Гематомантия")
            bleed_access_gives_use_to_thing = input()
            print("Ботаника")
            nature_access_gives_use_to_thing = input()
            print("Псифистика")
            mental_access_gives_use_to_thing = input()
            print("Владение навыками Колющего оружия")
            twohanded_access_gives_use_to_thing = input()
            print("Владение навыками Режущего оружия")
            polearm_access_gives_use_to_thing = input()
            print("Владение навыками Дробящего оружия")
            onehanded_access_gives_use_to_thing = input()
            print("Владение навыками Двуручного оружия")
            stabbing_access_gives_use_to_thing = input()
            print("Владение навыками Древкового оружия")
            cutting_access_gives_use_to_thing = input()
            print("Владение навыками Одноручного оружия")
            crushing_access_gives_use_to_thing = input()
            print("Владение навыками Стрелкового оружия")
            small_arms_access_gives_use_to_thing = input()
            print("Владение навыками щитов")
            shields_access_gives_use_to_thing = input()

            print("\n" + "Введите получаемые полоски за экипировку и использование предмета: ")
            print("Полоска здоровья")
            health_max_gives_use_to_thing = input()
            print("Полоска ментального здоровья")
            mind_max_gives_use_to_thing = input()
            print("Полоска выносливости")
            stamina_max_gives_use_to_thing = input()
            print("Полоска маны")
            mana_max_gives_use_to_thing = input()
            print("Полоска голода")
            hunger_max_gives_use_to_thing = input()
            print("Полоска интоксикации")
            intoxication_max_gives_use_to_thing = input()

            print("\n" + "Введите получаемые очки экипировки и использования, занимаемые артефактом: ")
            print("Шлем")
            helmet_status_gives_use_to_thing = input()
            print("Нагрудник")
            chest_status_gives_use_to_thing = input()
            print("Ботинки")
            shoes_status_gives_use_to_thing = input()
            print("Наручи")
            gloves_status_gives_use_to_thing = input()
            print("Предметы экипировки")
            item_slot_gives_use_to_thing = input()

            print("\n" + "Введите колличество дающих разрешений, дающего артефактом при экипировке и использовании: ")
            i = int(input())
            z = 0
            list_of_permissions_use_to = []
            for z in range(i):
                print("Введите требование " + str(z) + ":")
                permission = int(input())
                list_of_permissions_use_to.append(permission)

            with open("Things/requirements" + ".json", "w") as json_file:
                json.dump(idk_1, json_file)
                json_file.close()
            with open("Things/requirements" + ".json", "w") as json_file:
                json.dump(idk_2, json_file)
                json_file.close()
            with open("Things/requirements" + ".json", "w") as json_file:
                json.dump(idk_3, json_file)
                json_file.close()
            with open("Things/requirements" + ".json", "w") as json_file:
                json.dump(idk_4, json_file)
                json_file.close()

            equip_to = {
                "SP_EQUIP_TO": sp_equip_to,
                "MP_EQUIP_TO": mp_equip_to,
                "IP_EQUIP_TO": ip_equip_to,
                "PP_EQUIP_TO": pp_equip_to,
                "AP_EQUIP_TO": ap_equip_to,
                "FP_EQUIP_TO": fp_equip_to,
                "LP_EQUIP_TO": lp_equip_to,
                "CP_EQUIP_TO": cp_equip_to,
                "BP_EQUIP_TO": bp_equip_to,
                "FIRE_ACCESS_EQUIP_TO_THING": fire_access_equip_to_thing,
                "WATER_ACCESS_EQUIP_TO_THING": water_access_equip_to_thing,
                "WIND_ACCESS_EQUIP_TO_THING": wind_access_equip_to_thing,
                "DIRT_ACCESS_EQUIP_TO_THING": dirt_access_equip_to_thing,
                "LIGHTNING_ACCESS_EQUIP_TO_THING": lightning_access_equip_to_thing,
                "HOLY_ACCESS_EQUIP_TO_THING": holy_access_equip_to_thing,
                "CURSE_ACCESS_EQUIP_TO_THING": curse_access_equip_to_thing,
                "BLEED_ACCESS_EQUIP_TO_THING": bleed_access_equip_to_thing,
                "NATURE_ACCESS_EQUIP_TO_THING": nature_access_equip_to_thing,
                "MENTAL_ACCESS_EQUIP_TO_THING": mental_access_equip_to_thing,
                "TWOHANDED_ACCESS_EQUIP_TO_THING": twohanded_access_equip_to_thing,
                "POLEARM_ACCESS_EQUIP_TO_THING": polearm_access_equip_to_thing,
                "ONEHANDED_ACCESS_EQUIP_TO_THING": onehanded_access_equip_to_thing,
                "STABBING_ACCESS_EQUIP_TO_THING": stabbing_access_equip_to_thing,
                "CUTTING_ACCESS_EQUIP_TO_THING": cutting_access_equip_to_thing,
                "CRUSHING_ACCESS_EQUIP_TO_THING": crushing_access_equip_to_thing,
                "SMALL_ARMS_ACCESS_EQUIP_TO_THING": small_arms_access_equip_to_thing,
                "SHIELDS_ACCESS_EQUIP_TO_THING": shields_access_equip_to_thing,
                "HELMET_STATUS_EQUIP_TO_THING": helmet_status_equip_to_thing,
                "CHEST_STATUS_EQUIP_TO_THING": chest_status_equip_to_thing,
                "SHOES_STATUS_EQUIP_TO_THING": shoes_status_equip_to_thing,
                "GLOVES_STATUS_EQUIP_TO_THING": gloves_status_equip_to_thing,
                "ITEM_SLOT_EQUIP_TO_THING": item_slot_equip_to_thing,
            }
            with open("Things/EQUIP_TO/" + str(id_permission_equip_to) + ".json", "w") as json_file:
                json.dump(equip_to, json_file)
                json_file.close()
            use_to = {
                "SP_USE_TO": sp_use_to,
                "MP_USE_TO": mp_use_to,
                "IP_USE_TO": ip_use_to,
                "PP_USE_TO": pp_use_to,
                "AP_USE_TO": ap_use_to,
                "FP_USE_TO": fp_use_to,
                "LP_USE_TO": lp_use_to,
                "CP_USE_TO": cp_use_to,
                "BP_USE_TO": bp_use_to,
                "FIRE_ACCESS_USE_TO_THING": fire_access_use_to_thing,
                "WATER_ACCESS_USE_TO_THING": water_access_use_to_thing,
                "WIND_ACCESS_USE_TO_THING": wind_access_use_to_thing,
                "DIRT_ACCESS_USE_TO_THING": dirt_access_use_to_thing,
                "LIGHTNING_ACCESS_USE_TO_THING": lightning_access_use_to_thing,
                "HOLY_ACCESS_USE_TO_THING": holy_access_use_to_thing,
                "CURSE_ACCESS_USE_TO_THING": curse_access_use_to_thing,
                "BLEED_ACCESS_USE_TO_THING": bleed_access_use_to_thing,
                "NATURE_ACCESS_USE_TO_THING": nature_access_use_to_thing,
                "MENTAL_ACCESS_USE_TO_THING": mental_access_use_to_thing,
                "TWOHANDED_ACCESS_USE_TO_THING": twohanded_access_use_to_thing,
                "POLEARM_ACCESS_USE_TO_THING": polearm_access_use_to_thing,
                "ONEHANDED_ACCESS_USE_TO_THING": onehanded_access_use_to_thing,
                "STABBING_ACCESS_USE_TO_THING": stabbing_access_use_to_thing,
                "CUTTING_ACCESS_USE_TO_THING": cutting_access_use_to_thing,
                "CRUSHING_ACCESS_USE_TO_THING": crushing_access_use_to_thing,
                "SMALL_ARMS_ACCESS_USE_TO_THING": small_arms_access_use_to_thing,
                "SHIELDS_ACCESS_USE_TO_THING": shields_access_use_to_thing,
                "HELMET_STATUS_USE_TO_THING": helmet_status_use_to_thing,
                "CHEST_STATUS_USE_TO_THING": chest_status_use_to_thing,
                "SHOES_STATUS_USE_TO_THING": shoes_status_use_to_thing,
                "GLOVES_STATUS_USE_TO_THING": gloves_status_use_to_thing,
                "ITEM_SLOT_USE_TO_THING": item_slot_use_to_thing,
                "LIST_OF_REQUIREMENTS": list_of_requirements,
                "AMOUNT_OF_REQUIREMENTS": amount_of_requirements
            }
            with open("Things/USE_TO/" + str(id_permission_use_to) + ".json", "w") as json_file:
                json.dump(use_to, json_file)
                json_file.close()
            able_to_equip = {
                "SP_GIVES": sp_gives_equip_to,
                "MP_GIVES": mp_gives_equip_to,
                "IP_GIVES": ip_gives_equip_to,
                "PP_GIVES": pp_gives_equip_to,
                "AP_GIVES": ap_gives_equip_to,
                "FP_GIVES": fp_gives_equip_to,
                "LP_GIVES": lp_gives_equip_to,
                "CP_GIVES": cp_gives_equip_to,
                "BP_GIVES": bp_gives_equip_to,
                "FIRE_RES_GIVE_THING": fire_res_gives_equip_to,
                "WATER_RES_GIVE_THING": water_res_gives_equip_to,
                "WIND_RES_GIVE_THING": wind_res_gives_equip_to,
                "DIRT_RES_GIVE_THING": dirt_res_gives_equip_to,
                "LIGHTNING_RES_GIVE_THING": lightning_res_gives_equip_to,
                "HOLY_RES_GIVE_THING": holy_res_gives_equip_to,
                "CURSE_RES_GIVE_THING": curse_res_gives_equip_to,
                "CRUSH_RES_GIVE_THING": crush_res_gives_equip_to,
                "CUT_RES_GIVE_THING": cut_res_gives_equip_to,
                "STAB_RES_GIVE_THING": stab_res_gives_equip_to,
                "CRUSH_DAMAGE_GIVES_THING": crush_damage_gives_equip_to,
                "CUT_DAMAGE_GIVES_THING": cut_damage_gives_equip_to,
                "STAB_DAMAGE_GIVES_THING": stab_damage_gives_equip_to,
                "HELMET_STATUS_GIVES_THING": helmet_status_gives_equip_to_thing,
                "CHEST_STATUS_GIVES_THING": chest_status_gives_equip_to_thing,
                "SHOES_STATUS_GIVES_THING": shoes_status_gives_equip_to_thing,
                "GLOVES_STATUS_GIVES_THING": gloves_status_gives_equip_to_thing,
                "ITEM_SLOT_GIVES_THING": item_slot_gives_equip_to_thing,
                "LIST_PERMISSION_GIVES": list_of_permissions_equip_to
            }
            with open("Things/ABLE_TO_EQUIP/" + str(id_gives_equip_to) + ".json", "w") as json_file:
                json.dump(able_to_equip, json_file)
                json_file.close()
            able_to_use = {
                "SP_GIVES": sp_gives_use_to,
                "MP_GIVES": mp_gives_use_to,
                "IP_GIVES": ip_gives_use_to,
                "PP_GIVES": pp_gives_use_to,
                "AP_GIVES": ap_gives_use_to,
                "FP_GIVES": fp_gives_use_to,
                "LP_GIVES": lp_gives_use_to,
                "CP_GIVES": cp_gives_use_to,
                "BP_GIVES": bp_gives_use_to,
                "FIRE_RES_GIVE_THING": fire_res_gives_use_to,
                "WATER_RES_GIVE_THING": water_res_gives_use_to,
                "WIND_RES_GIVE_THING": wind_res_gives_use_to,
                "DIRT_RES_GIVE_THING": dirt_res_gives_use_to,
                "LIGHTNING_RES_GIVE_THING": lightning_res_gives_use_to,
                "HOLY_RES_GIVE_THING": holy_res_gives_use_to,
                "CURSE_RES_GIVE_THING": curse_res_gives_use_to,
                "CRUSH_RES_GIVE_THING": crush_res_gives_use_to,
                "CUT_RES_GIVE_THING": cut_res_gives_use_to,
                "STAB_RES_GIVE_THING": stab_res_gives_use_to,
                "FIRE_DAMAGE_GIVES_THING": fire_damage_gives_use_to,
                "WATER_DAMAGE_GIVES_THING": water_damage_gives_use_to,
                "WIND_DAMAGE_GIVES_THING": wind_damage_gives_use_to,
                "DIRT_DAMAGE_GIVES_THING": dirt_damage_gives_use_to,
                "LIGHTNING_DAMAGE_GIVES_THING": lightning_damage_gives_use_to,
                "HOLY_DAMAGE_GIVES_THING": holy_damage_gives_use_to,
                "CURSE_DAMAGE_GIVES_THING": curse_damage_gives_use_to,
                "CRUSH_DAMAGE_GIVES_THING": crush_damage_gives_use_to,
                "CUT_DAMAGE_GIVES_THING": cut_damage_gives_use_to,
                "STAB_DAMAGE_GIVES_THING": stab_damage_gives_use_to,
                "CLEAR_DAMAGE_GIVES_THING": clear_damage_gives_use_to,
                "FIRE_ACCESS_GIVES_THING": fire_access_gives_use_to_thing,
                "WATER_ACCESS_GIVES_THING": water_access_gives_use_to_thing,
                "WIND_ACCESS_GIVES_THING": wind_access_gives_use_to_thing,
                "DIRT_ACCESS_GIVES_THING": dirt_access_gives_use_to_thing,
                "LIGHTNING_ACCESS_GIVES_THING": lightning_access_gives_use_to_thing,
                "HOLY_ACCESS_GIVES_THING": holy_access_gives_use_to_thing,
                "CURSE_ACCESS_GIVES_THING": curse_access_gives_use_to_thing,
                "BLEED_ACCESS_GIVES_THING": bleed_access_gives_use_to_thing,
                "NATURE_ACCESS_GIVES_THING": nature_access_gives_use_to_thing,
                "MENTAL_ACCESS_GIVES_THING": mental_access_gives_use_to_thing,
                "TWOHANDED_ACCESS_GIVES_THING": twohanded_access_gives_use_to_thing,
                "POLEARM_ACCESS_GIVES_THING": polearm_access_gives_use_to_thing,
                "ONEHANDED_ACCESS_GIVES_THING": onehanded_access_gives_use_to_thing,
                "STABBING_ACCESS_GIVES_THING": stabbing_access_gives_use_to_thing,
                "CUTTING_ACCESS_GIVES_THING": cutting_access_gives_use_to_thing,
                "CRUSHING_ACCESS_GIVES_THING": crushing_access_gives_use_to_thing,
                "SMALL_ARMS_ACCESS_GIVES_THING": small_arms_access_gives_use_to_thing,
                "SHIELDS_ACCESS_GIVES_THING": shields_access_gives_use_to_thing,
                "HEALTH_MAX_GIVES_THING": health_max_gives_use_to_thing,
                "MIND_MAX_GIVES_THING": mind_max_gives_use_to_thing,
                "STAMINA_MAX_GIVES_THING": stamina_max_gives_use_to_thing,
                "MANA_MAX_GIVES_THING": mana_max_gives_use_to_thing,
                "HUNGER_MAX_GIVES_THING": hunger_max_gives_use_to_thing,
                "INTOXICATION_MAX_GIVES_THING": intoxication_max_gives_use_to_thing,
                "HELMET_STATUS_GIVES_THING": helmet_status_gives_use_to_thing,
                "CHEST_STATUS_GIVES_THING": chest_status_gives_use_to_thing,
                "SHOES_STATUS_GIVES_THING": shoes_status_gives_use_to_thing,
                "GLOVES_STATUS_GIVES_THING": gloves_status_gives_use_to_thing,
                "ITEM_SLOT_GIVES_THING": item_slot_gives_use_to_thing,
                "LIST_PERMISSION_GIVES": list_of_permissions_use_to
            }
            with open("Things/ABLE_TO_USE/" + str(id_gives_use_to) + ".json", "w") as json_file:
                json.dump(able_to_use, json_file)
                json_file.close()
            thing = {
                'THING_NAME': thing_name,
                'THING_STATUSES':
                    {
                        'ARTEFACT_WEARED_THING': 0,
                        'COSTS_THING_BUY': cost_thing_buy,
                        'COSTS_THING_SELL': cost_thing_sell,
                        'COST_PER_REPUTATION': 0,
                        'DURABILITY_MAX': durability_max,
                        'DURABILITY_NOW': durability_now,
                        'WEIGHT_GIVES': weight,
                    },
                'REQUIREMENTS':
                    {
                        'EQUIP_TO': equip_to,
                        'USE_TO': use_to
                    },
                'THING_GIVE':
                    {
                        'ABLE_TO_EQUIP': able_to_equip,
                        'ABLE_TO_USE': able_to_use
                    }
            }
            with open("Things/THING/" + thing_name + ".json", "w") as json_file:
                json.dump(thing, json_file)
                json_file.close()

def maker_starter():
    print("что вы хотите сделать?"+"\n"+"Чтобы добавить расу введите 1. "+"\n"+"Чтобы добавить артефакт введите 2.")
    x = int(input())
    if x == 1:
        raceCreate()
    if x == 2:
        thingCreate()
    if x != 1 & x !=2:
        print("Неверная команда, попробуйте ещё раз.")
        maker_starter()


maker_starter()
