# quocheck
Random healthcheck quotes for an API

# Usage

    from quocheck impot Quocheck
    
    
    @app.route('/health')
    def health():
        """
        Returns: radnom healthcheck quote
        """
        return jsonify(Quocheck().get_quote())
