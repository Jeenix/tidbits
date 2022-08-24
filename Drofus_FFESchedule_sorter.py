import pandas as pd

# NOTE: UI for users to set which columns, or is this too much?


def main():
    APPEND_NAME = "_IMPORT"  #add to new file that it writes to
    path = r"P:\19\1904010.000\Design\BIM\_Revit\5.0 Project Resources\01 Scripts\Python\FFE Schedule Testing\20220819_Birthing_FFESchedule.xlsx"
    df1 = pd.read_excel(path)
    df_length = df1.shape[0]  #number of rows
    rooms_dict = create_dict_rls_rooms(df1)
    write_to_file(rooms_dict)


#----------------------- get dict of unique room numbers


def create_dict_rls_rooms(df1):
    columns = list(df1)
    rooms_dict = {}
    item_number_col = columns[0]
    for rows in df1[item_number_col]:
        rooms_dict.update({rows: " "})
    # print(unique_rooms)

    for room in rooms_dict:
        room_info_list = df1.loc[df1[item_number_col] == room]
        rooms_dict.update({room: room_info_list})

    return rooms_dict


#-----------------------print to excel


def write_to_file(rooms_dict):
    writer = pd.ExcelWriter(path, engine='xlsxwriter')

    df1.to_excel(writer, sheet_name='x1')
    df2.to_excel(writer, sheet_name='x2')
    writer.save()
    writer.close()


if __name__ == '__main__':
    main()