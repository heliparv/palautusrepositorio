from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All

class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr))

    def oneOf(self, *queries):
        for query in queries:
            if QueryBuilder(query):
                return QueryBuilder(query)
