from scraper.scraper_class import Scraper
from unittest.mock import patch


#Implement test cases for this task:
#Filter all previous entries with more than five words in the title, ordered by the number of comments first.
def test_title_has_more_than_five_words():
    s = Scraper()
    assert s._title_has_more_than_five_words("This title has more than five words") is True
    assert s._title_has_more_than_five_words("One two three four five") is False
    assert s._title_has_more_than_five_words("Exactly six words in this title") is True
    assert s._title_has_more_than_five_words("   Lots   of   spaces   here   ") is False
    assert s._title_has_more_than_five_words("._, ,¿.,. .¿* ,.,. .=,. ,. ,.++ ,.,") is False
    assert s._title_has_more_than_five_words("With ,¿.,. signs ,.,. .=,. ,. ,.++ ,.,") is False

#Implement test cases for this task:
#Filter all previous entries with less than or equal to five words in the title, ordered by points.
def test_title_has_five_or_fewer_words():
    s = Scraper()
    assert s._title_has_five_or_fewer_words("Short title here") is True
    assert s._title_has_five_or_fewer_words("This is a longer title here") is False
    assert s._title_has_five_or_fewer_words("Just five words here") is True
    assert s._title_has_five_or_fewer_words("   Extra   spaces   count   too   ") is True
    assert s._title_has_five_or_fewer_words("._, ,¿.,. .¿* ,.,. .=,. ,. ,.++ ,.,") is True  
    assert s._title_has_five_or_fewer_words("Only, two...words!!") is True
    

#Test cases for the score points
def test_extract_score():
    s = Scraper()
    assert s._extract_score("123 points") == 123
    assert s._extract_score("42 points") == 42
    assert s._extract_score("No points") == 0
    assert s._extract_score("") == 0
    assert s._extract_score("points 32") == 32


#Test cases for comment count
def test_extract_comment_count():
    s = Scraper()
    assert s._extract_comment_count("56 comments") == 56
    assert s._extract_comment_count("comments 22 comments") == 22
    assert s._extract_comment_count("1\xa0comment") == 1
    assert s._extract_comment_count("23\xa0comments") == 23
    assert s._extract_comment_count("No comments") == 0
    assert s._extract_comment_count("") == 0

#Test cases for clean title
def test_clean_title():
    s = Scraper()
    assert s._clean_title("Title title (2023)") == "Title title"
    assert s._clean_title("Another title") == "Another title"
    assert s._clean_title("A title with (parentheses) at end (remove me)") == "A title with (parentheses) at end"
    assert s._clean_title("Title (title) of (title)") == "Title (title) of"
    assert s._clean_title("(Only info)") == ""
    assert s._clean_title("") == ""
    assert s._clean_title("   ") == ""
    assert s._clean_title("Title with trailing spaces   ") == "Title with trailing spaces"
    assert s._clean_title("Ending with space and (info)   ") == "Ending with space and"
    assert s._clean_title("Ti.tle with 100% -- characters") == "Ti.tle with 100% -- characters"

#Test cases for short titles sorted by score
def test_filter_entries_with_short_titles_by_score():
    mock_data = [
        {
            'title': 'Short title here',
            'score': '50 points',
            'comments': '30 comments'
        },
        {
            'title': 'This title is definitely too long for the filter',
            'score': '100 points',
            'comments': '60 comments'
        },
        {
            'title': 'Tiny title',
            'score': '75 points',
            'comments': '10 comments'
        },
    ]

    expected_titles = ['Tiny title', 'Short title here']
    with patch.object(Scraper, '_load_json_file', return_value=mock_data):
        s = Scraper()
        result = s.filter_entries_with_short_titles_by_score()
        assert len(result) == 2
        assert [entry['title'] for entry in result] == expected_titles


#Test cases for long titles sorted by the number of comments
def test_filter_entries_by_title_words_from_file():
    mock_data = [
        {
            'title': 'This title has more than five words exactly',
            'score': '80 points',
            'comments': '40 comments'
        },
        {
            'title': 'Short one here',
            'score': '95 points',
            'comments': '70 comments'
        },
        {
            'title': 'Another very long title for testing filter',
            'score': '60 points',
            'comments': '90 comments'
        },
    ]

    expected_titles = [
        'Another very long title for testing filter',
        'This title has more than five words exactly'
    ]

    with patch.object(Scraper, '_load_json_file', return_value=mock_data):
        s = Scraper()
        result = s.filter_entries_by_title_words_from_file()
        assert len(result) == 2  
        assert [entry['title'] for entry in result] == expected_titles