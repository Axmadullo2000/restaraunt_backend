
Чтобы получит все данные ставим GET запрос api/restorans/func/

Чтобы добавить новую колонку ставим:
POST запрос api/restorans/func/ обязательные параметры: name, adress,phone,rate,range_money,type_cook,photo_one, photo_two.

Чтобы получить конкретную таблицу из бд ставим GET запрос api/restorans/func/{id}/

Чтобы изменить конкретную таблицу ставим PUT запрос api/restorans/func/{id}/
обязательные параметры: name, adress,phone,rate,range_money,type_cook,photo_one, photo_two.

Чтобы удалить конкретную таблицу из бд ставим запрос DELETE api/restorans/func/{id}/

Чтобы получить доступ к админке проходите в admin/ и вводите name:cool_guy и password:1