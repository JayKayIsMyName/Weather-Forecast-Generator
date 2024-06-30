##########################################################
#                                                        #
#       coordinates_validator.py                         #
#       Ensures given coordinates are a valid input      #
#       (within acceptable bounds for latitude           #
#       and longitude)                                   #
#                                                        #
#       Created by Beau Smith                            #
#                                                        #
##########################################################

def validate_coordinates(latitude, longitude):

    try:

        # (attempts to) convert lat/lon into float values
        lat = float(latitude)
        lon = float(longitude)

        # checks to see if coordinates are valid values
        if -90 <= lat <= 90 and -180 <= lon <= 180:

            # returns lat/lon values if valid
            return lat, lon
        
        else:

            # returns two None values if not
            return None, None
        
    except ValueError:

        # returns two None values if lat/lon cannot be converted into float values
        return None, None
