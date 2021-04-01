
# quocheck
Random healthcheck quotes for an API

# Installaton

    git submodule add https://github.com/jkarpichev/quocheck.git

# Usage

    from quocheck impot Quocheck
    
    
    @app.route('/health')
    def health():
        """
        Returns: radnom healthcheck quote
        """
        return jsonify(Quocheck().get_quote())
