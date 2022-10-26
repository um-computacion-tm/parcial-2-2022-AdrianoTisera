FROM python

RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-AdrianoTisera

WORKDIR /parcial-2-2022-AdrianoTisera

CMD ["python", "-m", "unittest"]