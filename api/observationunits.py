
import helper

observation_names = ["collector", "observationDbId",
            "observationTimeStamp", "observationVariableDbId",
            "observationVariableName", "season", "value"]
treatment_names = ["factor", "modality"]

names_map = {
    "observationvariabledbid": "observationVariableDbId",
    "observationvariablename": "observationVariableName",
    "observationdbid": "observationDbId",
    "observationtimestamp": "observationTimeStamp",
    "studydbid": "studyDbId",
    "observationtreatment": "observationtreatment",
    "treatmentdbid": "treatmentDbId",
    "observationunitname": "observationUnitName"
}

def search(germplasmDbId=None, observationVariableDbId=None, studyDbId=None, locationDbId=None, trialDbId=None, programDbId=None, seasonDbId=None, observationLevel=None, observationTimeStampRangeStart=None, observationTimeStampRangeEnd=None, pageSize=None, page=None):

    if observationTimeStampRangeStart:
        observationTimeStampRangeStart = deserialize_datetime(observationTimeStampRangeStart)

    if observationTimeStampRangeEnd:
        observationTimeStampRangeEnd = deserialize_datetime(observationTimeStampRangeEnd)


    params = []
    query = "select v.id::text as observationVariableDbId,  \
                    v.name as observationVariableName,  \
                    t.id::text as observationDbId, \
                    t.mean::text as value, \
                    t.date as observationTimeStamp, \
                    s.sitename as observationUnitName, \
                    es.experiment_id::text as studyDbId, \
                    et.treatment_id as treatmentDbId, \
                    treatments.name as season, \
                    treatments.definition as observationtreatment \
             from traits t, variables v, sites s, experiments_sites es, experiments_treatments et, treatments treatments  \
             where v.id = t.variable_id \
             and t.site_id = s.id \
             and es.site_id = t.site_id \
             and et.experiment_id = es.experiment_id \
             and treatments.id=et.treatment_id"

    # For not, observationVariable is variable
    # e.g.,  6000000007 plant_height 
    if observationVariableDbId:
        query += " and v.id = %s "
        params.append(observationVariableDbId)

    # For now, location is site
    if locationDbId:
        query += " and t.site_id = %s "
        params.append(locationDbId)

    if studyDbId:
        query += " and es.experiment_id = %s "
        params.append(studyDbId)

    # For now, germplasm is cultivar
    if germplasmDbId:
        query += " and t.cultivar_id = %s "
        params.append(germplasmDbId)

    if (observationTimeStampRangeStart and observationTimeStampRangeEnd):
        query += " and (date >= %s and date <= %s)"
        params.append(observationTimeStampRangeStart)
        params.append(observationTimeStampRangeEnd)
    elif observationTimeStampRangeStart:
        query += " and date >= %s"
        params.append(observationTimeStampRangeStart)
    elif observationTimeStampRangeEnd:
        query += " and date <= %s"
        params.append(observationTimeStampRangeEnd)

    count = helper.query_count(query, params)
    res = helper.query_result(query, params, pageSize, page)
    data = _conform_data([dict(r) for r in res])

    # split data if needed, remembering total number
    if not pageSize:
        pageSize = helper.DEFAULT_PAGE_SIZE
    if not page:
        page = 0

    return helper.create_result({"data": data}, count, pageSize, page)


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
         return string

def _conform_data(data):
    if not isinstance(data, list):
        return data

    return [_conform_element(x) for x in data]

def _conform_element(ele):
    if not isinstance(ele, dict):
        return ele

    res_obs = {}
    res_treat = {}
    res = {}
    for k,v in ele.items():
        if k in names_map:
            k = names_map[k]
        if k in observation_names:
            res_obs[k] = v
        elif k in treatment_names:
            res_treat[k] = v
        else:
            res[k] = v

    if len(res_obs.keys()) > 0:
        res["observations"] = [res_obs]
    if len(res_treat.keys()) > 0:
        res["treatments"] = [res_treat]

    return res

