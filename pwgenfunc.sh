function pwgen {
    if ! $1; then
        pwcnt=16
    else
        pwcnt=${1}
    fi
    if ! -f /opt/homebrew/opt/pwgen/bin/pwgen; then
        echo "pwgen executable does not exist. Exiting."
        exit 0
    fi
    pwgencmd="/opt/homebrew/opt/pwgen/bin/pwgen -csy 16 ${pwcnt}"

    eval ${pwgencmt}
    
}