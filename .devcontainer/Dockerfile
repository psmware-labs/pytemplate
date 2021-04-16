FROM python:3.9-slim
LABEL author="Pat McLean" \
      maintainer="Pat McLean<pmclean@vso-inc.com>"
# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
COPY ./.devcontainer/.bashrc /root/

# Setting up user access
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && apt-get install --no-install-recommends -y \
    make \
    gcc \
    wget \
    libpq-dev \
    libpython3-dev \
    git \
    gnupg \
    less \
    zsh \
    zip \
    curl \
    vim \
    openssh-client \
    sudo \
    curl

WORKDIR /app
RUN echo "===> Creating Python Packages tools user and group..." \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/zsh --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && chown -fR $USERNAME:$USERNAME /app
USER ${USERNAME}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN echo "===> Setting up development user shell..."
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" \
    && touch /home/$USERNAME/.z
COPY ./.devcontainer/.zshrc  /home/$USERNAME/

RUN echo "===> Installing Python Packages tools... "
RUN /home/$USERNAME/.poetry/bin/poetry config virtualenvs.create false
COPY ./pyproject.toml /app/pyproject.toml
COPY ./poetry.lock /app/poetry.lock
RUN /home/$USERNAME/.poetry/bin/poetry install

# Setting up user access
USER root
RUN echo "===> Setting up development user sudo access..." \
    # Add sudo support for non-root user
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
RUN chown -fR $USERNAME:$USERNAME /home/$USERNAME \
    && echo "===> Cleaning up package list..." \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -fR /root/*.txt



