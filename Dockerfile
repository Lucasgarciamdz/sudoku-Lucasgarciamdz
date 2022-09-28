FROM python:3
RUN git clone https://github.com/Lucasgarciamdz/sudoku-Lucasgarciamdz.git
WORKDIR sudoku-Lucasgarciamdz
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]