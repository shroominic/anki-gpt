FROM shroominic/python-uv

COPY pyproject.toml pyproject.toml

RUN uv pip install -r pyproject.toml

COPY ankigpt /ankigpt

ENV PATH="/.venv/bin:$PATH"

CMD fastapi run ankigpt --host 0.0.0.0
