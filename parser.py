import pyparsing as pp


class Parser():
    
    def __init__(self):
        pass
        
    def parse(self, query):
        title = pp.CaselessKeyword("Title")("field")
        year = pp.CaselessKeyword("Year")("field")
        rating = pp.CaselessKeyword("Rating")("field")
        
        title_only_operators = pp.one_of("== !=").set_name("title comparison operator (== or !=)")
        operator = pp.one_of("== != < > <= >=").set_name("comparison operator (== != < > <= >=)")
        
        movie_name = pp.QuotedString('"').set_name("movie name in quotes")
        
        get = pp.CaselessKeyword("Get")
        get_field = (year | rating)("get_field")
        
        #get statement follows a title statement optionally
        optional_get_statement = pp.Optional(get + get_field)
        
        #grammar 1
        title_statement = title + title_only_operators("op") + movie_name("value") + optional_get_statement
        
        #grammar 2
        num_value = pp.pyparsing_common.number.set_name("numeric value")
        year_statement = year + operator("op") + num_value("value")
        
        #grammar 3
        
        rating_statement = rating + operator("op") + num_value("value")
        
        #each condition grouped so chained conditions don't flatten 
        condition = pp.Group(title_statement ^ year_statement ^ rating_statement)
        
        #connecting multiple statements with AND/OR
        connectors = pp.one_of("and or", caseless=True).set_name("connector (and/or)")
        connectors = connectors.set_parse_action(lambda t: t[0].lower())
        
        expression = condition + pp.ZeroOrMore(connectors + condition)
        
        try:
            result = expression.parse_string(query, parse_all=True)
        except pp.ParseBaseException as e:
            return {"error": str(e)}
        
        conditions = []
        connectors_found = []
        get_field_found = None
        
        
        #creating a dictionary that allows for multiple combined queries 
        for token in result:
            if isinstance(token, pp.ParseResults):
                conditions.append({
                    "field": token.field,
                    "op": token.op,
                    "value": token.value,
                })
                if token.get_field:
                    get_field_found = token.get_field
            else:
                connectors_found.append(token)
        #returning a dictionary that has condtions which is the different chunks of the queries, 
        # connections which is the pieces that connect the queries 
        #and then a get which would go at the end of a query
        return {
            "conditions": conditions,
            "connectors": connectors_found,
            "get": get_field_found,
        }



# parser = Parser()
    
# print(parser.parse('Title == "The Shawshank Redemption" and Year > 2000 '))
