class CSVWriter:
    def output_csv(self, output_csv_path, output_text_path):
        spell = Speller()

        # Create a single CSV file for all aggregated information
        output_file_path_csv = os.path.join(output_csv_path, "aggregated_data.csv")
        with open(output_file_path_csv, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Add headers for dates, extract_terms, names, hospital, and Seq
            header_row = ['Name', 'Date', 'Time', 'Hospital', 'Filt', 'Seq'] + [f'{term}_Value' for term in extract_terms] + \
                         ['Mask', 'CRA', 'L Values', 'Tilt values', 'Resolution Values']
            csv_writer.writerow(header_row)

            for filename in os.listdir(output_text_path):
                if filename.lower().endswith('.txt'):
                    input_file_path = os.path.join(output_text_path, filename)

                    with open(input_file_path, 'r') as input_file:
                        extracted_text = input_file.read()
                        dates = extract_dates(extracted_text)
                        names = extract_most_likely_name(extracted_text)

                        if names is None or 'Li-' in names:
                            continue
                        correct_names = [spell(name) for name in [names]]  # Correct the single name
                        hosp_lines = extract_hosp(extracted_text)
                        correct_hosp = [spell(line) for line in hosp_lines]
                        seq_numbers = extract_seq(extracted_text)
                        filt_numbers = extract_filt(extracted_text)
                        mask_numbers = extract_mask(extracted_text)
                        CRA_numbers = extract_CRA(extracted_text)
                        L_values = extract_L(extracted_text)
                        tilt_values = extract_tilt(extracted_text)
                        time_values = extract_time(extracted_text)
                        resolution_values = extract_resolution(extracted_text)

                        for name in correct_names:
                            for date in dates:
                                for time in time_values:
                                    row_values = [name, date, time]

                                    row_values.append(' '.join(correct_hosp))
                                    row_values.append(' '.join(filt_numbers))
                                    row_values.append(' '.join(seq_numbers))

                                    for term in extract_terms:
                                        values = extract_values(extracted_text, term)
                                        row_values.append(values[0][1].strip('.').strip() if values else '')

                                    row_values.append(' '.join(mask_numbers))
                                    row_values.append(' '.join(CRA_numbers))
                                    row_values.append(' '.join(L_values))
                                    row_values.append(' '.join(tilt_values))
                                    row_values.append(' '.join(resolution_values))

                                    csv_writer.writerow(row_values)

        print("Aggregated CSV file created.")
