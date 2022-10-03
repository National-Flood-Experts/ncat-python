import requests
from src.Exceptions import CannotConnectToNCATException, RequiredParameterMissingException, NCATTimeoutException


class NCAT:
    base_uri = 'https://geodesy.noaa.gov/api/ncat/'
    connect_timeout = 6
    timeout = 10

    def llh(self, parameters):
        required_llh_parameters = ['lat', 'lon', 'inDatum', 'outDatum']
        return self.__make_request('llh', required_llh_parameters, parameters)

    def spc(self, parameters):
        required_spc_parameters = ['northing', 'easting', 'inDatum', 'outDatum', 'spcZone']
        return self.__make_request('spc', required_spc_parameters, parameters)

    def utm(self, parameters):
        """
        According to the NCAT documentation, the "spcZone" parameter is
        required for a UTM request. However, requests can be made without
        it. Since the documentation says it is required, we will check
        for it before making a request

        More information below:
        https://geodesy.noaa.gov/web_services/ncat/utm-service.shtml
        """

        required_utm_parameters = ['northing', 'easting', 'inDatum', 'outDatum', 'spcZone', 'utmZone']
        return self.__make_request('utm', required_utm_parameters, parameters)

    def xyz(self, parameters):
        required_xyz_parameters = ['x', 'y', 'z', 'inDatum', 'outDatum']
        return self.__make_request('xyz', required_xyz_parameters, parameters)

    def usng(self, parameters):
        required_usng_parameters = ['usng', 'inDatum', 'outDatum']
        return self.__make_request('usng', required_usng_parameters, parameters)

    @staticmethod
    def __check_for_required_parameters(required_parameters, given_parameters):
        for key in required_parameters:
            if key not in given_parameters:
                raise RequiredParameterMissingException(key)

    @staticmethod
    def __build_query_string(parameters):
        query_string = ''

        for key, value in parameters.items():
            query_string = query_string + key + '=' + str(value) + '&'

        return query_string[0:len(query_string) - 1]

    def __make_request(self, endpoint, required_parameters, given_parameters):
        try:
            self.__check_for_required_parameters(required_parameters, given_parameters)
            query_string = self.__build_query_string(given_parameters)
            response = requests.get(self.base_uri + endpoint + '?' + query_string,
                                    timeout=(self.connect_timeout, self.timeout))
            return response.json()
        except ConnectionError as error:
            raise CannotConnectToNCATException(error)
        except TimeoutError:
            raise NCATTimeoutException()
