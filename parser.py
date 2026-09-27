import pyparsing as pp


class Parser():
    
    def __init__(self):
        #using the replace with to make the fields lowercase
        title = pp.CaselessKeyword("Title").set_parse_action(pp.replace_with("title"))("field")
        year = pp.CaselessKeyword("Year").set_parse_action(pp.replace_with("year"))("field")
        rating = pp.CaselessKeyword("Rating").set_parse_action(pp.replace_with("rating"))("field")
        box_office = pp.CaselessKeyword("Box Office").set_parse_action(pp.replace_with("box_office"))("field")

        title_only_operators = pp.one_of("== !=").set_name("title comparison operator (== or !=)")
        operator = pp.one_of("== != < > <= >=").set_name("comparison operator (== != < > <= >=)")
        
        movie_name = pp.QuotedString('"').set_name("movie name in quotes")
        
        get = pp.CaselessKeyword("Get")
        get_field = (year | rating | box_office)("get_field")
        
        #get statement is optional and goes at the end
        optional_get_statement = pp.Optional(pp.Suppress(get) + get_field)

        #grammar 1
        title_statement = title + title_only_operators("op") + movie_name("value")
        
        #grammar 2
        num_value = pp.pyparsing_common.number.set_name("numeric value")
        year_statement = year + operator("op") + num_value("value")
        
        #grammar 3
        
        rating_statement = rating + operator("op") + num_value("value")

        #grammar 4
        box_office_statement = box_office + operator("op") + num_value("value")

        #each condition grouped so it doesn't flatten
        condition = pp.Group(title_statement ^ year_statement ^ rating_statement ^ box_office_statement)
        
        #connecting two statements with AND/OR
        connectors = pp.one_of("and or", caseless=True).set_name("connector (and/or)")
        connectors = connectors.set_parse_action(lambda t: t[0].lower())
        
        #at most one AND/OR ]
        self.expression = condition + pp.Optional(connectors + condition) + optional_get_statement

    def parse(self, query):
        try:
            result = self.expression.parse_string(query, parse_all=True)
        except pp.ParseBaseException as e:
            return {"error": str(e)}
        
        conditions = []
        connectors_found = []
        get_field_found = result.get("get_field")

        #dropping the get field before we loop through
        tokens = result[:-1] if get_field_found else result

        #creating a dictionary that allows for multiple combined queries
        for token in tokens:
            if isinstance(token, pp.ParseResults):
                conditions.append({
                    "field": token.field,
                    "op": token.op,
                    "value": token.value,
                })
            else:
                connectors_found.append(token)
        #returning a dictionary that has condtions which is the different chunks of the queries, 
        # connections is the AND/ OR  that connect the queries 
        #and then a get which would go at the end of a query
        return {
            "conditions": conditions,
            "connectors": connectors_found,
            "get": get_field_found,
        }



parser = Parser()
    
print(parser.parse('Title == "The Shawshank Redemption" Get Rating'))
