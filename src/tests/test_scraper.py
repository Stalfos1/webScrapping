from scraper.scraper_class import Scraper

def test_title_has_more_than_five_words():
    s = Scraper()
    assert s._title_has_more_than_five_words("This title has more than five words") is True
    assert s._title_has_more_than_five_words("One two three four five") is False
    assert s._title_has_more_than_five_words("Exactly six words in this title") is True
    assert s._title_has_more_than_five_words("   Lots   of   spaces   here   ") is False
    assert s._title_has_more_than_five_words("._, ,¿.,. .¿* ,.,. .=,. ,. ,.++ ,.,") is False
    assert s._title_has_more_than_five_words("With ,¿.,. signs ,.,. .=,. ,. ,.++ ,.,") is False



def test_title_has_five_or_fewer_words():
    s = Scraper()
    assert s._title_has_five_or_fewer_words("Short title here") is True
    assert s._title_has_five_or_fewer_words("This is a longer title here") is False
    assert s._title_has_five_or_fewer_words("Just five words here") is True
    assert s._title_has_five_or_fewer_words("   Extra   spaces   count   too   ") is True
    assert s._title_has_five_or_fewer_words("._, ,¿.,. .¿* ,.,. .=,. ,. ,.++ ,.,") is True  
    assert s._title_has_five_or_fewer_words("Only, two...words!!") is True