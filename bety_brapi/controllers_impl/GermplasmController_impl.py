import json

from bety_brapi import helper

def germplasm_search_get(germplasmPUI, germplasmDbId, germplasmName, commonCropName, pageSize, page):
    """
    Search for a specific germplasm. Right now this will use an external file to get all the information.
    :param germplasmPUI:
    :param germplasmDbId:
    :param germplasmName:
    :param commonCropName:
    :param pageSize:
    :param page:
    :return:
    """

    # load all the data
    # TODO this does not work if pakcage is installed, need to use pkgutil
    file = 'data/germplasm.json'
    data = json.load(open(file, 'r'))

    # filter the data
    if germplasmPUI:
        data = [x for x in data if x.get('germplasmPUI', '') == germplasmPUI]
    if germplasmDbId:
        data = [x for x in data if x.get('germplasmDbId', '') == int(germplasmDbId)]
    if germplasmName:
        data = [x for x in data if x.get('germplasmName', '') == germplasmName]
    if commonCropName:
        data = [x for x in data if x.get('commonCropName', '') == commonCropName]

    # split data if needed, remembering total number
    count = len(data)
    if not pageSize:
        pageSize = helper.DEFAULT_PAGE_SIZE
    if not page:
        page = 0
    data = data[page * pageSize:(page+1) * pageSize]

    # return the resulting data
    return helper.create_result({"data": data}, count, pageSize, page)


def treatments_by_experiment_get(experimentId):

    params = list()

    # get all sitegroups and sites
    query = ""

    query = "SELECT experiments_treatments.experiment_id as experimentId, " \
            "   experiments_treatments.treatment_id as treatmentId, " \
            "   treatments.name as treatmentName, " \
            "   treatments.definition as treatmentDefinition " \
            "FROM experiments_treatments INNER JOIN treatments ON experiments_treatments.treatment_id=treatments.id " \
            "WHERE experiments_treatments.experiment_id = "+experimentId

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params)
    # wrap result
    data = []
    for row in results:
        entry = dict()
        treatment = dict()
        entry['experiment_id'] = row["experimentid"]
        treatment["treatment_id"] = row["treatmentid"]
        treatment["treatment_name"] = row["treatmentname"]
        treatment["treatment_definition"] = row["treatmentdefinition"]
        entry["treatments"] = treatment
        data.append(entry)
    return helper.create_result({"treatments": data}, count)


def treatments_by_experiment_post(experiment_ids_list):

    experiment_ids_list = str(experiment_ids_list)
    experiment_ids_list = experiment_ids_list.replace('[','(')
    experiment_ids_list = experiment_ids_list.replace(']',')')


    params = list()
    # get all sitegroups and sites
    query = ""

    query = "SELECT experiments_treatments.experiment_id as experimentId, " \
            "   experiments_treatments.treatment_id as treatmentId, " \
            "   treatments.name as treatmentName, " \
            "   treatments.definition as treatmentDefinition " \
            "FROM experiments_treatments INNER JOIN treatments ON experiments_treatments.treatment_id=treatments.id " \
            "WHERE experiments_treatments.experiment_id IN " + experiment_ids_list

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params)
    # wrap result
    data = []
    for row in results:
        entry = dict()
        treatment = dict()
        entry['experiment_id'] = row["experimentid"]
        treatment["treatment_id"] = row["treatmentid"]
        treatment["treatment_name"] = row["treatmentname"]
        treatment["treatment_definition"] = row["treatmentdefinition"]
        entry["treatments"] = treatment
        data.append(entry)
    return helper.create_result({"treatments": data}, count)


def cultivars_by_experiment_post(experiment_ids_list):

    experiment_ids_list = str(experiment_ids_list)
    experiment_ids_list = experiment_ids_list.replace('[','(')
    experiment_ids_list = experiment_ids_list.replace(']',')')


    params = list()
    # get all sitegroups and sites

    query = "SELECT experiments_sites.experiment_id as experimentid, " \
            "   sites_cultivars.site_id as siteid, " \
            "   cultivars.specie_id as species, " \
            "   sites_cultivars.cultivar_id as cultivarid, " \
            "   species.scientificname as scientificname, " \
            "   cultivars.name as cultivarname " \
            "FROM experiments_sites, sites_cultivars, cultivars, species " \
            "WHERE experiments_sites.site_id=sites_cultivars.site_id " \
            "AND  sites_cultivars.cultivar_id=cultivars.id " \
            "AND  species.id=cultivars.specie_id " \
            "AND experiments_sites.experiment_id IN " + experiment_ids_list

    # count first
    count = helper.query_count(query, params)

    # execute query
    results = helper.query_result(query, params)
    # wrap result
    data = []
    for row in results:
        entry = dict()
        cultivar = dict()
        entry['experiment_id'] = row["experimentid"]
        cultivar["cultivar_name"] = row["cultivarname"]
        cultivar["cultivar_id"] = row["cultivarid"]
        cultivar['specie_id'] = row["species"]
        cultivar['scientific_name'] = row['scientificname']
        entry["cultivar"] = cultivar
        data.append(entry)
    return helper.create_result({"treatments": data}, count)