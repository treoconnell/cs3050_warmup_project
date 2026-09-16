import pyparsing as pp


class Parser():
    
    def __init__(self):
        pass
    
    def parse(self, query):
        
        
        
        title = pp.Keyword("Title")
        year = pp.Keyword("Year")
        rating = pp.Keyword("Rating")
        
        title_only_operators = pp.one_of("== !=")
        operator = pp.one_of("== != < > <= >=")
        
        value = pp.QuotedString('"')
        
        get = pp.Keyword("Get")
        
        #get statement follows a title statement optionally
        optional_get_statement = pp.Optional(get + year | get + rating )
        
        #grammar 1
        title_statement = title + title_only_operators + value + optional_get_statement
        
        #grammar 2
        
        year_statement = year + operator + value
        
        #grammar 3
        
        rating_statement = rating + operator + value
        return title_statement.parse_string(query)
    
parser = Parser()
    
print(parser.parse('Title == "Airbuds 2" Get Year'))