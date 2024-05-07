DROP TABLE IF EXISTS cities;

CREATE VIRTUAL TABLE cities USING fts5(title, lat, lon);

INSERT INTO cities(title, lat, lon)
VALUES
    ('Абакан', 53.7209, 91.4424),
    ('Архангельск', 64.5393, 40.5187),
    ('Астана', 71.4305, 51.1284),
    ('Астрахань', 46.3478, 48.0335),
    ('Барнаул', 53.3561, 83.7496),
    ('Белгород', 50.5974, 36.5888),
    ('Бийск', 52.5414, 85.2196),
    ('Бишкек', 42.8710, 74.5945),
    ('Благовещенск', 50.2907, 127.5272),
    ('Братск', 56.1514, 101.6342),
    ('Брянск', 53.2434, 34.3642),
    ('Великий Новгород', 58.5215, 31.2755),
    ('Владивосток', 43.1340, 131.9284),
    ('Владикавказ', 43.0241, 44.6905),
    ('Владимир', 56.1290, 40.4070),
    ('Волгоград', 48.7071, 44.5169),
    ('Вологда', 59.2205, 39.8916),
    ('Воронеж', 51.6615, 39.2003),
    ('Грозный', 43.3180, 45.6982),
    ('Донецк', 48.0159, 37.8028),
    ('Екатеринбург', 56.8380, 60.5973),
    ('Иваново', 57.0003, 40.9739),
    ('Ижевск', 56.8528, 53.2115),
    ('Иркутск', 52.2864, 104.2807),
    ('Казань', 55.7958, 49.1066),
    ('Калининград', 55.9162, 37.8545),
    ('Калуга', 54.5070, 36.2523),
    ('Каменск-Уральский', 56.4149, 61.9189),
    ('Кемерово', 55.3596, 86.0878),
    ('Киев', 50.4024, 30.5327),
    ('Киров', 54.0790, 34.3232),
    ('Комсомольск-на-Амуре', 50.5499, 137.0079),
    ('Королев', 55.9162, 37.8545),
    ('Кострома', 57.7677, 40.9264),
    ('Краснодар', 45.0239, 38.9702),
    ('Красноярск', 56.0087, 92.8705),
    ('Курск', 51.7304, 36.1926),
    ('Липецк', 52.6102, 39.5947),
    ('Магнитогорск', 53.4117, 58.9844),
    ('Махачкала', 42.9849, 47.5046),
    ('Минск', 53.9061, 27.5549),
    ('Москва', 55.7558, 37.6178),
    ('Мурманск', 68.9696, 33.0745),
    ('Набережные Челны', 55.7436, 52.3958),
    ('Нижний Новгород', 56.3239, 44.0023),
    ('Нижний Тагил', 57.9101, 59.9813),
    ('Новокузнецк', 53.7865, 87.1552),
    ('Новороссийск', 44.7235, 37.7687),
    ('Новосибирск', 55.0287, 82.9069),
    ('Норильск', 69.3490, 88.2010),
    ('Омск', 54.9893, 73.3682),
    ('Орел', 52.9703, 36.0635),
    ('Оренбург', 51.7681, 55.0974),
    ('Пенза', 53.1945, 45.0195),
    ('Первоуральск', 56.9081, 59.9429),
    ('Пермь', 58.0048, 56.2377),
    ('Прокопьевск', 53.8954, 86.7447),
    ('Псков', 57.8194, 28.3318),
    ('Ростов-на-Дону', 47.2272, 39.7450),
    ('Рыбинск', 58.1385, 38.5736),
    ('Рязань', 54.6199, 39.7450),
    ('Самара', 53.1955, 50.1018),
    ('Санкт-Петербург', 59.9388, 30.3143),
    ('Саратов', 51.5315, 46.0358),
    ('Севастополь', 44.6166, 33.5254),
    ('Северодвинск', 64.5582, 39.8296),
    ('Северодвинск', 64.5582, 39.8296),
    ('Симферополь', 44.9521, 34.1024),
    ('Сочи', 43.5815, 39.7229),
    ('Ставрополь', 45.0445, 41.9691),
    ('Сухум', 43.0157, 41.0251),
    ('Тамбов', 52.7212, 41.4522),
    ('Ташкент', 41.3143, 69.2673),
    ('Тверь', 56.8596, 35.9119),
    ('Тольятти', 53.5113, 49.4181),
    ('Томск', 56.4951, 84.9721),
    ('Тула', 54.1930, 37.6178),
    ('Тюмень', 57.1530, 65.5343),
    ('Улан-Удэ', 51.8335, 107.5841),
    ('Ульяновск', 54.3170, 48.4022),
    ('Уфа', 54.7348, 55.9578),
    ('Хабаровск', 48.4726, 135.0577),
    ('Харьков', 49.9935, 36.2304),
    ('Чебоксары', 56.1439, 47.2489),
    ('Челябинск', 55.1598, 61.4025),
    ('Шахты', 47.7085, 40.2160),
    ('Энгельс', 51.4989, 46.1251),
    ('Южно-Сахалинск', 46.9591, 142.7381),
    ('Якутск', 62.0278, 129.7042),
    ('Ярославль', 57.6266, 39.8938)