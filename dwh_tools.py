# functionalities to retrieve data from DWH
# A) surface stations
# B) vertical profiles


def dwh_surface(station_id, date_start, date_end, print_steps):
    '''
    retrieve observations from surface station

    input:
    station_id      string      'PAY'
    date_start      string      '20210912000000'
    date_end        string      '20210913000000'
    print_steps     Boolean

    output:
    pandas dataframe
    '''

    cmd = (
        "/oprusers/osm/bin/retrieve_cscs --show_records -j lat,lon,name,wmo_ind -s surface"
        #insert the command from confluence page
        + " -i nat_abbr," # -i int_ind
        + station_id
        + " -p "
        + "1547,1541"  # e.g 742,743,745,746,747,748 choose and extract all columns containing relevant paramenters (i.e. all except the pressure column.)
        + " -t "
        + date_start
        + "-"
        + date_end
        + " --use-limitation 50"   #" -C 34"
    )
    print("--- calling: " + cmd)
    # ~~~~~~~~~~~~~~~ the following code was taken from the dwh2pandas.py script by Claire Merker ~~~~~~~~~~~~~~~
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        shell=True,
    )
    # ~~~~~~~~~~~~~~~ check if cmd can be executed ~~~~~~~~~~~~~~~
    try:
        out, err = proc.communicate(timeout=120)
    except subprocess.TimeoutExpired:
        proc.kill()
        out, err = proc.communicate()
        raise SystemExit("--- ERROR: timeout expired for process " + cmd)
    if proc.returncode != 0:
        raise SystemExit(err)

    # ~~~~~~~~~~~~~~~ load DWH retrieve output into pandas DataFrame ~~~~~~~~~~~~~~~
    header_line = pd.read_csv(
        StringIO(out), skiprows=0, nrows=1, sep="\s+", header=None, engine="c"
    )

    # parse the command linen output
    data = pd.read_csv(
        StringIO(out),
        skiprows=2,
        skipfooter=2,
        sep="|",
        header=None,
        names=header_line.values.astype(str)[0, :],
        engine="python",
        parse_dates= ["termin"],
    )

    # clean up the dataframe a bit
    data.replace(1e7, np.nan, inplace=True)

    # check if no data is available for the time period
    if data.empty:
        raise SystemExit("--- WARN: no data available for " + date_start + ".")
    else:
        if print_steps:
            with pd.option_context(
                "display.max_rows",
                None,
                "display.max_columns",
                None,
                "display.width",
                1000,
            ):
                print(data.head())
        print("--- data retrieved into dataframe")
        return data


def dwh_profile(station_id, date, print_steps):
    '''
    retrieve observations of atmospheric vertical profile

    input:
    station_id      string      '06610'
    date            string      '20210912000000'
    print_steps     Boolean

    output:
    pandas dataframe
    '''
    cmd = (
        "/oprusers/osm/bin/retrieve_cscs --show_records -j lat,lon,elev,name,wmo_ind -w 22 -s profile -p "
        + "742,743,745,746,747,748"  # extract all columns containing relevant paramenters (i.e. all except the pressure column.)
        + " -i int_ind,"
        + station_id
        + " -t "
        + date
        + "-"
        + date
        + " -C 34"
    )
    print("--- calling: " + cmd)
    # ~~~~~~~~~~~~~~~ the following code was taken from the dwh2pandas.py script by Claire Merker ~~~~~~~~~~~~~~~
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        shell=True,
    )
    # ~~~~~~~~~~~~~~~ check if cmd can be executed ~~~~~~~~~~~~~~~
    try:
        out, err = proc.communicate(timeout=120)
    except subprocess.TimeoutExpired:
        proc.kill()
        out, err = proc.communicate()
        raise SystemExit("--- ERROR: timeout expired for process " + cmd)
    if proc.returncode != 0:
        raise SystemExit(err)

    # ~~~~~~~~~~~~~~~ load DWH retrieve output into pandas DataFrame ~~~~~~~~~~~~~~~
    header_line = pd.read_csv(
        StringIO(out), skiprows=0, nrows=1, sep="\s+", header=None, engine="c"
    )

    # parse the command linen output
    data = pd.read_csv(
        StringIO(out),
        skiprows=2,
        skipfooter=2,
        sep="|",
        header=None,
        names=header_line.values.astype(str)[0, :],
        engine="python",
        parse_dates=["termin"],
    )

    # clean up the dataframe a bit
    data.replace(1e7, np.nan, inplace=True)

    # check if no data is available for the time period
    if data.empty:
        raise SystemExit("--- WARN: no data available for " + date + ".")
    else:
        if print_steps:
            with pd.option_context(
                "display.max_rows",
                None,
                "display.max_columns",
                None,
                "display.width",
                1000,
            ):
                print(data.head())
        print("--- data retrieved into dataframe")
        return data