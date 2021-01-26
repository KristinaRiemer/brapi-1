def search(studyDbId=None, observationUnitDbId=None, eventDbId=None, eventType=None, dateRangeStart=None,
           dateRangeEnd=None, pageSize=None, page=None):
    query = "SELECT DISTINCT experiments.id::text as studyDbId, " \

def get(studyDbId, observationUnitDbId, eventDbId):

