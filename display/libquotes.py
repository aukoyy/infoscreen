import random


def get_random_ben_quote():
    rand_num = random.randint(0, 12)
    return ben_quotes()[rand_num]


def ben_quotes():
    quote_list = [
        'Temperance. Eat not to dullness; drink not to elevation.',
        'Silence. Speak not but what may benefit others or yourself; avoid trifling conversation.',
        'Order. Let all your things have their places; let each part of your business have its time.',
        'Resolution. Resolve to perform what you ought; perform without fail what you resolve.',
        'Frugality. Make no expense but to do good to others or yourself; i.e., waste nothing.',
        'Industry. Lose no time; be always employ\'d in something useful; cut off all unnecessary actions.',
        'Sincerity. Use no hurtful deceit; think innocently and justly, and, if you speak, speak accordingly.',
        'Justice. Wrong none by doing injuries, or omitting the benefits that are your duty.',
        'Moderation. Avoid extremes; forbear resenting injuries so much as you think they deserve.',
        'Cleanliness. Tolerate no uncleanliness in body, cloaths, or habitation.',
        'Tranquillity. Be not disturbed at trifles, or at accidents common or unavoidable.',
        'Chastity. Rarely use venery but for health or offspring, never to dullness, weakness, '
        'or the injury of your own or another\'s peace or reputation.',
        'Humility. Imitate Jesus and Socrates.'
    ]
    return quote_list


