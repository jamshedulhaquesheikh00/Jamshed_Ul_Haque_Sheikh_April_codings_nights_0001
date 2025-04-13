if st.button(f"Download (files.name) as (format_choice)"):
    output = BytesIO()
    if format_choice == "csv":
        df.to_csv(output, index=False)
        mime = "text/csv"
        if not files.name.endswith(".csv"):
            new_name = files.name.replace(ext, "csv")
        else:
            new_name = files.name
    else:
        df.to_excel(output, index=False, engine='openpyxl')
        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        if not file.name.endswith(".xlsx"):
            new_name = file.name.replace(ext, "xlsx")
        else:
            new_name = files.name
    output.seek(0)
    st.download_button("Download file", filename=new_name, data=output, mime=mime, help="Click to download the converted file")
    st.info("Processing Complete!")